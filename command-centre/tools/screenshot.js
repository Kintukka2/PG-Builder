// Screenshot a local preview in dark, light and phone layouts.
// Usage: NODE_PATH=$(npm root -g) node screenshot.js <out-dir> <preview.html>
// Reports horizontal overflow and console errors for each layout.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const out = process.argv[2], url = 'file://' + process.argv[3];
  const errs = [];
  for (const [name, vp, scheme] of [['desk-dark',{width:1440,height:900},'dark'],['desk-light',{width:1440,height:900},'light'],['mobile-dark',{width:400,height:860},'dark']]) {
    const p = await b.newPage({viewport: vp, colorScheme: scheme});
    p.on('console', m => { if (m.type() === 'error') errs.push(name + ': ' + m.text()); });
    p.on('pageerror', e => errs.push(name + ' pageerror: ' + e.message));
    await p.goto(url); await p.waitForTimeout(2500);
    await p.screenshot({path: `${out}/${name}.png`, fullPage: true});
    const ow = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    console.log(name, 'overflowX', ow);
    await p.close();
  }
  console.log('errors:', JSON.stringify(errs.slice(0,10)));
  await b.close();
})();
