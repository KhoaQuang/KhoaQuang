function validatePassword(password: string): boolean {
    return password.length >= 6;
}

console.log(validatePassword("123456"))
console.log(validatePassword("123"))