from pgxml import *
R = 'D365 End-user'
ENTITY = ('*Check* the **Entity**.', 'Confirm you are signed into the correct **Legal Entity** (top-right). To change it, see [[GS_T3_1|3.1 Switch Legal Entity with the Selector]].')
ACCESS = 'Access to D365.'

def proc_intro(text): return [h5('Procedure'), lead(text)]

def sub(n, anchor, title, desc, init, intro, prereqs, steps, end, extra_after=None, resp_text=None, pagebreak=True):
    o = [heading(4, title, anchor, pagebreak=pagebreak, toc_text=f'{n} {title}'), blank(), h5('Description')]
    o += [body(x) for x in desc] + [bodyblank(), h5('Responsibility'), bullet(resp_text or f'{R}: {RESP.get(anchor, "completes this task in their own D365 session.")}'),
          bodyblank(), h5('Initiation')] + [bullet(x) for x in init] + [bodyblank()]
    o += proc_intro(intro) + [procedure(prereqs, R, steps, end)]
    if extra_after: o += extra_after
    return o

RESP = {}

def topic(n, anchor, title, desc, resp, init, overview=None, first=False):
    o = [heading(3, title, anchor, pagebreak=not first, toc_text=f'{n}. {title}')]
    o += topic_block(desc, resp, init, overview)
    return o

def part2a():
    o = [heading(2, 'Part 2: How do I do it? (Getting Started)', 'GS_Part2', numbered=False, pagebreak=True), blank()]
    # ---------------- 1 Session
    o += topic(1, 'GS_T1', 'Set Up Your D365 Session',
        ['Use this topic to sign in to D365, set the user options that control how D365 opens and shows dates and numbers, and change the session date when a task needs a different date.'],
        [f'{R}: sets up and manages their own D365 session.'],
        ['A new user starts using D365, or a user needs to change their settings or the session date.'],
        overview=[('GS_T1_1', '1.1 Sign In and Sign Out', 'Open D365 in the browser, sign in with your work account, and sign out when you finish.'),
                  ('GS_T1_2', '1.2 Set Your User Options', 'Set your default legal entity, start page, language, date and number format, and time zone.'),
                  ('GS_T1_3', '1.3 Change the Session Date', 'Optional. Change the date D365 uses by default for the current session, then reset it.')], first=True)
    o += sub('1.1', 'GS_T1_1', 'Sign In and Sign Out',
        ['Use this procedure to open D365 in your browser and sign in with your WiseTech Global work account, and to sign out at the end of your work. '
         'D365 runs in a web browser; Microsoft recommends the latest Microsoft Edge.'],
        ['A user starts or finishes their D365 work.'],
        'Complete these steps to sign in to D365:',
        ['Your manager has requested your D365 profile.', 'A supported browser, such as Microsoft Edge.'],
        [('*Open* your browser.', 'Open Microsoft Edge (recommended) or another supported browser.'),
         ('*Enter* the **D365 URL**.', ['Enter the D365 address in the address bar: https://wtg.operations.dynamics.com. {{Confirm the address and whether users open D365 from a bookmark or the Atlas site.}}'],
          'GS-04: Confirm the D365 URL users open, the sign-in method (work account, multifactor authentication) and how users sign out (the initials menu on the navigation bar), in the clean-session test with IT. Microsoft has no end-user article on signing in.'),
         ('*Sign in* with your work account.', 'Sign in with your WiseTech Global email address and password, and approve the sign-in request if one is shown.'),
         ('*Confirm* the **Dashboard** is displayed.', 'D365 opens on the dashboard, or on the initial page set in your user options, in your default legal entity.'),
         ('*Select* your initials to sign out.', 'When you finish, select your initials at the right of the navigation bar, then select **Sign out**. Save your work first.')],
        ('step', ['You are signed in to D365.'], ('GS_T1_2', '1.2 Set Your User Options')),
        extra_after=[note('D365 signs you out after a period without activity. A countdown message appears first: select it to stay signed in. Unsaved changes are lost when the session closes.')])
    RESP['GS_T1_2'] = 'sets their own user options.'
    o += sub('1.2', 'GS_T1_2', 'Set Your User Options',
        ['Use this procedure to set the options that apply to you on every page: the legal entity D365 opens in, the page it opens on, and your language, date, time, number format and time zone. '
         'Changes take effect when you save.'],
        ['A new user sets up D365, or a user’s legal entity, location or preferences change.'],
        'Complete these steps to set your user options:',
        ['You are signed in to D365 (see [[GS_T1_1|1.1 Sign In and Sign Out]]).'],
        [('*Click* **Settings**.', 'On the navigation bar, click **Settings** (the gear icon).'),
         ('*Select* **User options**.', 'Select **User options**. The **Options** page opens on the **Visual** tab, where you can choose a colour theme and the size of page elements.'),
         ('*Click* the **Preferences** tab.', 'Click **Preferences**.'),
         ('*Select* the **Company**.', 'On the **Startup** FastTab, select in **Company** the legal entity D365 opens in when you sign in.'),
         ('*Select* the **Initial page**.', 'Select the page D365 opens on, for example **Default dashboard**.'),
         ('*Check* the **Default view/edit mode**.', 'Leave the default unless your process guide says otherwise. It controls whether pages open locked for viewing or ready for editing.',
          'GS-05: Confirm the values offered in Default view/edit mode (Microsoft shows Auto; the values are not documented for users) and which the company recommends.'),
         ('*Select* the **Language**.', 'On the **Language and country/region preferences** FastTab, select your **Language**.'),
         ('*Select* the **Date, time, and number format**.', 'Select the format for your country, for example **en-AU**.'),
         ('*Select* the **Time zone**.', 'Select the time zone you work in, so dates and times show in your local time.'),
         ('*Click* **Save**.', 'Click **Save**. The options apply from now on.')],
        ('complete', ['D365 opens in your default legal entity and on your initial page, and shows dates, times and numbers in your format and time zone.']))
    RESP['GS_T1_3'] = 'changes the session date only when their task requires it.'
    o += sub('1.3', 'GS_T1_3', 'Change the Session Date',
        ['Use this procedure to change the date D365 uses by default for the current session, for example when a process guide tells you to enter transactions with an earlier date. '
         'The session date is the default date for new journals and documents. It applies to your current session only and returns to today when you sign out or the session closes.'],
        ['A process guide tells you to work with a date other than today.'],
        'Complete these steps to change the session date:',
        ['You are signed in to D365.', 'Your process guide tells you to use a different date.'],
        [('*Click* **Modules**.', 'From the left-hand **Navigation Pane**, click **Modules**.'),
         ('*Navigate* to the **Session date and time** page.', ['From the **Navigation Pane**, *select*:', '> Common >', '> Common >', '> Session date and time']),
         ('*Enter* the **Date**.', 'Enter the date your process guide gives.'),
         ('*Click* **OK**.', 'Click **OK**. New records in this session now default to that date.'),
         ('*Reset* the session date when you finish.', 'Repeat steps 1 to 4 with today’s date, or sign out, so later work is not dated by mistake.')],
        ('complete', ['D365 uses the date you entered as the default date for the rest of the session.']),
        extra_after=[important('A wrong session date gives new journals and documents the wrong date. Change it only when your process guide tells you to, and reset it as soon as you finish.',
                               comment='GS-06: Confirm the company rule on changing the session date: who may change it, for which tasks, and whether it must be reset. Microsoft documents the steps only.')])
    # ---------------- 2 Open a page
    o += topic(2, 'GS_T2', 'Open a Page',
        ['Use this topic to open the pages and workspaces you need: from the Navigation Pane, with the page search, from your Favorites, or from a workspace. Each process guide gives the path to its own pages.'],
        [f'{R}: opens the pages their work needs.'],
        ['A user needs a page or workspace for a task.'],
        overview=[('GS_T2_1', '2.1 Open a Page from the Navigation Pane', 'Open a page from its module menu, or from Recent.'),
                  ('GS_T2_2', '2.2 Search for a Page', 'Find a page by typing part of its name.'),
                  ('GS_T2_3', '2.3 Add/Remove Pages to Favorites', 'Mark the pages you use often, and remove them when you no longer need them.'),
                  ('GS_T2_4', '2.4 Work from a Workspace', 'Open a workspace and use its tiles, lists and links.')])
    RESP['GS_T2_1'] = 'opens the pages their work needs.'
    o += sub('2.1', 'GS_T2_1', 'Open a Page from the Navigation Pane',
        ['Use this procedure to open a page from its module menu in the Navigation Pane. Every process guide gives the path as a list of menu levels, for example **Accounts receivable > Customers > All customers**.'],
        ['A user needs a page and knows its navigation path.'],
        'Complete these steps to open a page from the Navigation Pane:',
        [ACCESS, 'The navigation path of the page, from your process guide.'],
        [ENTITY,
         ('*Click* **Modules**.', 'From the left-hand **Navigation Pane**, click **Modules**. If the pane is closed, click the menu icon at its top.'),
         ('*Click* the module.', 'Click the first level of the path, for example **Accounts receivable**. The module menu opens.'),
         ('*Click* the page.', 'Find the page under its menu heading, for example **Customers > All customers**, and click it.'),
         ('*Confirm* the page is open.', 'Check the page title. If the module or page is not shown, contact the BAU Support team (topic 13.3).')],
        ('complete', ['The page is open in the active legal entity.']),
        extra_after=[note('**Recent** in the **Navigation Pane** lists the pages you opened most recently. Use it to return to a page quickly.')])
    RESP['GS_T2_2'] = 'finds pages by name.'
    o += sub('2.2', 'GS_T2_2', 'Search for a Page',
        ['Use this procedure to find a page or workspace by typing words from its name. The search finds pages, not data: to find a customer, vendor or invoice, open its list page and filter it (topic 5).'],
        ['A user needs a page but does not know, or does not want to follow, its navigation path.'],
        'Complete these steps to search for a page:',
        [ACCESS],
        [('*Click* **Search for a page**.', 'On the navigation bar, click **Search for a page** (the magnifying glass), or press **Ctrl+/** or **Alt+G**.'),
         ('*Type* words from the page name.', 'Type one or more words, for example **payment journal**. Each result shows the page name and its navigation path.'),
         ('*Select* the page.', 'Select the page in the results. If it is not listed, add or change words: the search shows up to 10 results.'),
         ('*Confirm* the page is open.', 'Check the page title before you continue.')],
        ('complete', ['The page is open.']))
    RESP['GS_T2_3'] = 'adds the pages they use to their own Favorites.'
    o += sub('2.3', 'GS_T2_3', 'Add/Remove Pages to Favorites',
        ['Use this procedure to add a D365 page to your Favorites, so that it opens directly from **Favorites** in the **Navigation Pane**, and to remove it when you no longer need it. '
         'Each process guide lists the pages worth adding for its work.'],
        ['A new user sets up D365, or a page is used often.'],
        'Complete these steps to add a page to your Favorites:',
        ['Access to D365 and to the module that contains the page.'],
        [ENTITY,
         ('*Click* **Modules**.', 'From the left-hand **Navigation Pane**, click **Modules**.'),
         ('*Click* the module that contains the page.', 'Click the module, for example **Accounts payable**. The module menu opens.'),
         ('*Click* the favorite star for the page.', ['In the module menu, find the page and click the star next to it. The page is added to your **Favorites**.', 'Note: To add another page, repeat steps 2 to 4.']),
         ('*Click* **Favorites**.', 'From the left-hand **Navigation Pane**, click **Favorites**. Your favorites list is displayed.'),
         ('*Confirm* the page is listed.', 'Confirm that the page appears in your favorites list.')],
        ('complete', ['The page appears under **Favorites** in the **Navigation Pane** and opens from there.']),
        extra_after=[h5('Remove a Page from Favorites'), lead('Complete these steps to remove a page from your Favorites:'),
                     procedure(['The page is in your Favorites.'], R,
                               [('*Click* **Favorites**.', 'From the left-hand **Navigation Pane**, click **Favorites**.'),
                                ('*Click* the star for the page.', 'Click the filled star next to the page. The page is removed from Favorites; your access to it does not change.')],
                               ('complete', ['The page is no longer in your Favorites. It still opens from its module menu.']))])
    RESP['GS_T2_4'] = 'starts their work from the workspace for their area.'
    o += sub('2.4', 'GS_T2_4', 'Work from a Workspace',
        ['Use this procedure to open a workspace and use its parts. A workspace brings together the work of one area, for example customer payments or vendor invoices: '
         'summary tiles with counts, tabbed lists of records that need action, and links to related pages. Selecting a tile or a list row opens the records behind it.'],
        ['A user starts work in an area that has a workspace, as their process guide describes.'],
        'Complete these steps to work from a workspace:',
        ['Access to D365 and to the workspace.'],
        [ENTITY,
         ('*Click* **Workspaces**.', 'From the left-hand **Navigation Pane**, click **Workspaces**, or select the workspace tile on the dashboard.'),
         ('*Select* the workspace.', 'Select the workspace your process guide names.'),
         ('*Review* the summary tiles.', 'Each tile shows a count of records, for example unposted journals. Click a tile to open the list of those records.'),
         ('*Select* a tab in the lists.', 'In the workspace lists, select a tab to see the records it holds. Use the **Filter** box above the list to narrow it.'),
         ('*Click* a link.', 'Optional. Under **Links**, click a page to open it.'),
         ('*Return* to the dashboard.', 'When you finish, click **Home** in the **Navigation Pane**, or press **Alt+Shift+Home**.')],
        ('complete', ['You have opened the records or pages you need from the workspace.']),
        extra_after=[note('Some workspaces have a filter at the top that applies to the whole workspace, and a button on the Action Pane that sets them up for you. Your process guide explains the settings for its workspace.',
                          comment='GS-08: Confirm whether Immersive Home is switched on in our environment (10.0.44 or later). It replaces the dashboard as the start page and changes topics 1.1, 2.4 and 11.2.')])
    # ---------------- 3 Legal entity
    o += topic(3, 'GS_T3', 'Switch Legal Entity',
        ['Use this topic to change the legal entity you are working in. Every page shows the data of the active legal entity, so check it before every task and switch when the task needs another one.'],
        [f'{R}: works in the legal entity required for the task.'],
        ['A user needs to work in a legal entity other than the active one.'],
        overview=[('GS_T3_1', '3.1 Switch Legal Entity with the Selector', 'Select the legal entity by its business name in the legal entity selector.'),
                  ('GS_T3_2', '3.2 Switch Legal Entity Using the Ledger Code', 'Change the ledger code in the D365 URL when the code is known.')])
    RESP['GS_T3_1'] = 'works in the legal entity required for the task.'
    o += sub('3.1', 'GS_T3_1', 'Switch Legal Entity with the Selector',
        ['Use this procedure to switch to another legal entity with the legal entity selector on the navigation bar. It is the usual way to switch, and it lets you find the legal entity by its business name.'],
        ['A user needs to work in a legal entity other than the active one.'],
        'Complete these steps to switch legal entity with the selector:',
        ['Access to D365 and to the required legal entity.', 'The business name of the required legal entity.'],
        [('*Click* the legal entity selector.', 'On the navigation bar (top-right), click the legal entity selector. It shows the active legal entity. You can also press **Ctrl+Shift+O**.'),
         ('*Find* the required legal entity.', 'Find the legal entity by its business name, or type part of the name or ledger code to narrow the list.'),
         ('*Select* the legal entity.', 'Select the legal entity. D365 switches to it.'),
         ('*Confirm* the active legal entity.', ['Check that the selector now shows the required legal entity before you continue.', 'Note: The ledger code also shows in the URL after **cmp=**, for example https://wtg.operations.dynamics.com/?cmp=112a.'])],
        ('complete', ['D365 is working in the required legal entity.']),
        extra_after=[note('If a legal entity you need is not in the list, contact the BAU Support team (topic 13.3).')])
    RESP['GS_T3_2'] = 'works in the legal entity required for the task.'
    o += sub('3.2', 'GS_T3_2', 'Switch Legal Entity Using the Ledger Code',
        ['Use this procedure to switch legal entity by changing the ledger code in the D365 URL, when you know the D365 ledger code. It is quicker when you move between legal entities often.'],
        ['The D365 ledger code of the required legal entity is known, and switching through the URL is quicker.'],
        'Complete these steps to switch legal entity using the ledger code:',
        ['Access to D365 and to the required legal entity.', 'The D365 ledger code of the required legal entity.'],
        [('*Click* the browser address bar.', 'Click the address bar to edit the D365 URL.'),
         ('*Find* the ledger code in the URL.', ['Find **cmp=** in the URL. The value immediately after **cmp=** is the D365 ledger code; in this example it is 112a:', 'https://wtg.operations.dynamics.com/?cmp=112a&mi=LedgerJournalTable_CustPaym']),
         ('*Enter* the required ledger code.', 'Replace only the ledger code after **cmp=** with the required D365 ledger code. Leave the rest of the URL unchanged. Do not use the CargoWise code.'),
         ('*Press* **Enter**.', 'Press **Enter** to open D365 in the required legal entity.'),
         ('*Confirm* the active legal entity.', 'Check that the legal entity selector (top-right) shows the required legal entity before you continue.')],
        ('complete', ['D365 is working in the required legal entity.']))
    return o
