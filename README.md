# StrakerPlaywright


# Have looked at the below references
Assertions - https://playwright.dev/python/docs/test-assertions
Actions and Waits - https://playwright.dev/python/docs/actionability

# PyTest with Playwright
There are few standars mentioned here of how to use it
https://playwright.dev/python/docs/test-runners


# My Notes Referencing this to Selenium Java

1. is_visible() or wait_for is actually similar to implicit and explicit waits we have in Selenium
2. pytest looks similar to the testNg framework
3. Fixtures are similar to @BeforeTest and @AfterTest
    1. @BeforeTest and @AfterTest are similar to using fixtures with scope='function'
    2. @BeforeClass and @AfterClass are witn using scope='class'
    3. Similar to @BeforeSuite we have 'module'
    4. Used the same thing to do things like launch browser, login before a test is executed.
4. Method with test_ in pytest is similar to having @Test annotation in selenium java


# Other notes
1. Removed networkidle as Playwright docs says its discouraged.
    (Reference: https://playwright.dev/python/docs/api/class-frame#frame-wait-for-selector)
2. To using networkidle(is taking 13 seconds) is taking time compare to domcontentloaded(is taking only 7 seconds)
3. To using expections & errors ,here how to use it.
    (Reference:https://playwright.dev/python/docs/api/class-timeouterror)