const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    const { email } = await req.json()

    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return new Response(JSON.stringify({ error: 'invalid_email' }), {
        status: 400,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      })
    }

    const supabaseUrl = Deno.env.get('SUPABASE_URL')
    const serviceRoleKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')

    const dbRes = await fetch(`${supabaseUrl}/rest/v1/subscribers`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': serviceRoleKey!,
        'Authorization': `Bearer ${serviceRoleKey}`,
        'Prefer': 'return=minimal',
      },
      body: JSON.stringify({ email }),
    })

    if (!dbRes.ok) {
      const dbError = await dbRes.json()
      if (dbError.code === '23505') {
        return new Response(JSON.stringify({ error: 'already_subscribed' }), {
          status: 409,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        })
      }
      throw new Error('Database error')
    }

    const emailRes = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${Deno.env.get('RESEND_API_KEY')}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: 'PuntGuide <info@puntguide.com.au>',
        to: email,
        subject: "You're in — new Aussie bookmaker alerts are on",
        html: welcomeEmailHtml(email),
      }),
    })

    if (!emailRes.ok) {
      console.error('Resend error:', await emailRes.text())
    }

    return new Response(JSON.stringify({ success: true }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    })
  } catch (err) {
    console.error(err)
    return new Response(JSON.stringify({ error: 'server_error' }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    })
  }
})

function welcomeEmailHtml(email: string): string {
  return `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background:#f0f4f8;font-family:Inter,sans-serif;">
  <div style="max-width:580px;margin:40px auto;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <div style="background:#1a3a5c;padding:32px 40px;">
      <div style="font-size:22px;font-weight:700;color:#fff;letter-spacing:-0.02em;">PuntGuide</div>
      <div style="font-size:12px;color:rgba(255,255,255,0.6);margin-top:4px;">puntguide.com.au</div>
    </div>
    <div style="padding:40px;">
      <h1 style="font-size:24px;font-weight:700;color:#1a3a5c;margin:0 0 16px;letter-spacing:-0.02em;">You're on the list ✓</h1>
      <p style="font-size:15px;color:#4a5568;line-height:1.7;margin:0 0 24px;">
        We'll let you know whenever a new licensed Australian bookmaker goes live — so you're always first to know about new platforms, sign-up offers and odds.
      </p>
      <div style="background:#f7fafc;border-radius:8px;padding:24px;margin-bottom:24px;">
        <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:#718096;margin-bottom:12px;">While you wait</div>
        <a href="https://puntguide.com.au/best-betting-sites-australia.html" style="display:block;color:#2b6cb0;font-size:14px;font-weight:500;text-decoration:none;margin-bottom:8px;">→ Best betting sites in Australia right now</a>
        <a href="https://puntguide.com.au/all-betting-sites.html" style="display:block;color:#2b6cb0;font-size:14px;font-weight:500;text-decoration:none;margin-bottom:8px;">→ Full list of all 130+ Australian bookmakers</a>
        <a href="https://puntguide.com.au/fastest-payout-betting-sites-australia.html" style="display:block;color:#2b6cb0;font-size:14px;font-weight:500;text-decoration:none;">→ Fastest payout betting sites</a>
      </div>
      <p style="font-size:13px;color:#718096;line-height:1.6;margin:0;">
        You subscribed with ${email}. To unsubscribe reply to this email with "unsubscribe" in the subject line.
      </p>
    </div>
    <div style="background:#f7fafc;padding:20px 40px;border-top:1px solid #e2e8f0;">
      <p style="font-size:11px;color:#a0aec0;margin:0;line-height:1.6;">
        PuntGuide · puntguide.com.au · info@betguide.com.au<br>
        Gambling involves risk. Please bet responsibly. For help visit <a href="https://www.gamblinghelponline.org.au" style="color:#a0aec0;">gamblinghelponline.org.au</a>
      </p>
    </div>
  </div>
</body>
</html>`
}
