import { test, expect, chromium } from '@playwright/test';

test('Login on Android real device', async ({}) => {
  // Kết nối tới Chrome Android thật
  const browser = await chromium.connectOverCDP('http://localhost:9333');
//   const context = await browser.newContext();
  const [androidPage] = browser.contexts()[0].pages();
//   const androidPage = await context.newPage();

  await androidPage.goto('https://10.103.3.86/iview/views/index.jsf');

//   await androidPage.locator('text=Login').tap();

  console.log(await androidPage.title());

  await browser.close();
});