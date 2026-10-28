import asyncio
import json
from playwright.async_api import async_playwright

cookies = [
    {"name": "datr", "value": "YOUR_FB_DATR", "domain": ".facebook.com", "path": "/"},
    {"name": "sb", "value": "YOUR_FB_SB", "domain": ".facebook.com", "path": "/"},
    {"name": "ps_l", "value": "1", "domain": ".facebook.com", "path": "/"},
    {"name": "ps_n", "value": "1", "domain": ".facebook.com", "path": "/"},
    {"name": "c_user", "value": "YOUR_FB_C_USER", "domain": ".facebook.com", "path": "/"},
    {"name": "xs", "value": "YOUR_FB_XS_TOKEN", "domain": ".facebook.com", "path": "/"},
    {"name": "wd", "value": "1853x967", "domain": ".facebook.com", "path": "/"},
    {"name": "fr", "value": "YOUR_FB_FR_TOKEN", "domain": ".facebook.com", "path": "/"},
    {"name": "presence", "value": "YOUR_FB_PRESENCE", "domain": ".facebook.com", "path": "/"}
]

async def scrape_fb():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path="/home/your-vps-user/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome",
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            locale="es-ES"
        )
        await context.add_cookies(cookies)
        page = await context.new_page()

        urls = [
            ("about", "https://www.facebook.com/groups/YOUR_FB_GROUP_ID/about"),
            ("members_admins", "https://www.facebook.com/groups/YOUR_FB_GROUP_ID/members/admins"),
            ("main", "https://www.facebook.com/groups/YOUR_FB_GROUP_ID/")
        ]

        for label, url in urls:
            print(f"=== Scraping {label} ({url}) ===")
            try:
                resp = await page.goto(url, wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(5) # wait for dynamic rendering
                title = await page.title()
                current_url = page.url
                print(f"[{label}] Title: {title}")
                print(f"[{label}] Final URL: {current_url}")
                
                # Check text content
                text = await page.evaluate("() => document.body.innerText")
                with open(f"/tmp/fb_{label}.txt", "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"[{label}] Saved text ({len(text)} chars)")
                
                # Also save a screenshot to check state
                await page.screenshot(path=f"/tmp/fb_{label}.png")
            except Exception as e:
                print(f"[{label}] Error:", e)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_fb())
