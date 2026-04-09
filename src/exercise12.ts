function delay(seconds: number): Promise<void> {
    return new Promise<void> (resolve => {
        setTimeout(resolve, seconds * 1000)
    });
}

// Ví dụ để sử dụng function ở trên
async function run (): Promise<void> {
    console.log("Delaying for 1 seconds...")
    await delay(1)
    console.log("Done delaying!")
}

run()
