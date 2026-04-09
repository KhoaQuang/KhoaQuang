function loginResult(isSuccess: boolean): string {
    const result: Record<string, string> = {
        true: "Login successful",
        false: "Login failed"
    };
    return result[String(isSuccess)];
}

console.log(loginResult(true))
console.log(loginResult(false))