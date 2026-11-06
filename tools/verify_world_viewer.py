"""Drive the live world viewer in headless Chromium and report what it renders."""

import asyncio
import json
import sys

from playwright.async_api import async_playwright


URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8787/"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=[
            "--use-angle=swiftshader",
            "--enable-unsafe-swiftshader",
            "--disable-gpu-sandbox",
        ])
        page = await browser.new_page(viewport={"width": 1280, "height": 720})
        console, errors = [], []
        page.on("console", lambda m: console.append(f"{m.type}: {m.text}"))
        page.on("pageerror", lambda e: errors.append(str(e)))

        await page.goto(URL, wait_until="load")
        await page.wait_for_timeout(5000)

        state = await page.evaluate("""() => ({
          hasGenesis: !!window.__genesis,
          cells: window.__genesis ? window.__genesis.cells : -1,
          pop: document.getElementById('pop').textContent,
          turn: document.getElementById('turn').textContent,
          gen: document.getElementById('gen').textContent,
          elev: document.getElementById('elev').textContent,
          ptime: document.getElementById('ptime').textContent,
          fps: document.getElementById('fps').textContent,
          status: document.getElementById('status').textContent,
          cam: window.__genesis
            ? [window.__genesis.camera.position.x, window.__genesis.camera.position.y,
               window.__genesis.camera.position.z]
            : null
        })""")

        await page.click("#enter")
        await page.wait_for_timeout(500)
        await page.screenshot(path="runs/render/world_live.png")

        before = await page.evaluate(
            "window.__genesis ? [window.__genesis.camera.position.x, window.__genesis.camera.position.z] : null"
        )
        await page.keyboard.down("KeyW")
        await page.wait_for_timeout(900)
        await page.keyboard.up("KeyW")
        after = await page.evaluate(
            "window.__genesis ? [window.__genesis.camera.position.x, window.__genesis.camera.position.z] : null"
        )
        await page.wait_for_timeout(300)
        await page.screenshot(path="runs/render/world_moved.png")

        print(json.dumps({
            "state": state,
            "cam_before": before,
            "cam_after": after,
            "console": console[:15],
            "errors": errors[:10],
        }, indent=1))
        await browser.close()


asyncio.run(main())
