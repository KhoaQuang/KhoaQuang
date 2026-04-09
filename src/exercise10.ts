type Credentials = {
  username: string
  password: string
}

const validCred: Credentials = {
    username: "cqkhoa",
    password: "password"
}

const invalidCred: Credentials = {
    username: "cqkhoa",
    password: "pass"
}

async function loginTest(cred: Credentials): Promise<void> {
    //Step 1: Opening login page
    console.log("Opening login page")

    //Step 2: Entering username: <username>
    console.log(`Entering username: ${cred.username}`)

    //Step 3: Entering password
    console.log('Entering password')

    //Step 4: Validate password
    if (cred.password.length >= 6) {
        return console.log("Test passed")
    } else {
        return console.log("Test failed")
    }
}

loginTest(validCred)
loginTest(invalidCred)
