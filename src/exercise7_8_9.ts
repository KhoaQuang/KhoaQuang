async function openPage(): Promise<string> {
    return "Page opened";
}

async function fetchUser(): Promise<string> {
    const time_start = Date.now();
    while (Date.now() - time_start < 1000) {}
    return "User data loaded";
}

async function testFlow(): Promise<void> {
    const page = await openPage();
    console.log(page);
    const user = await fetchUser();
    console.log(user);
}

testFlow();