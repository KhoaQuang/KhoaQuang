# 📘 Week 0 Assignment – TypeScript Basics for Playwright

## 🎯 Objective

This assignment verifies that you have the **minimum TypeScript knowledge** required to start working with Playwright automation.

By completing this, you should be able to:

* Use basic TypeScript syntax (variables, functions, types)
* Work with arrays and objects
* Apply control flow for test logic
* Understand and use `async/await` (critical for Playwright)

---

## 📂 Submission Requirements

* Create a GitLab repository:

  ```
  week0-typescript-assignment
  ```

* Project structure:

  ```
  /src
    exercise1.ts
    exercise2.ts
    ...
  package.json
  tsconfig.json
  README.md
  ```

* Create your own branch based on week0 branch i.e week0_pttho, week0_cqkhoa

* Push your code to TMA GitLab: https://gitlab.tma.com.vn/users/sign_in

* Click Run button (TBD) to verify your code


---

## 🧩 Exercises

### 🔹 Section 1: Basic Syntax (10 points)

#### Exercise 1 (5 pts)

Create variables:

* `username: string`
* `age: number`
* `isLoggedIn: boolean`

Print all values.

---

#### Exercise 2 (5 pts)

Create function:

```ts
function greet(user: string): string
```

Return:

```
Hello, <user>
```

---

### 🔹 Section 2: Arrays & Objects (20 points)

#### Exercise 3 (10 pts)

* Create array of URLs
* Loop and print:

```
Navigating to: <url>
```

---

#### Exercise 4 (10 pts)

* Define type:

```ts
type User = {
  username: string
  password: string
}
```

* Create 2 users
* Print usernames

---

### 🔹 Section 3: Control Flow (20 points)

#### Exercise 5 (10 pts)

```ts
function validatePassword(password: string): boolean
```

* Valid if length ≥ 6

---

#### Exercise 6 (10 pts)

```ts
function loginResult(isSuccess: boolean): string
```

* Return:

  * `"Login successful"`
  * `"Login failed"`

---

### 🔹 Section 4: Async/Await (30 points) 🔥

#### Exercise 7 (10 pts)

```ts
async function openPage(): Promise<string>
```

Return `"Page opened"`

---

#### Exercise 8 (10 pts)

```ts
async function fetchUser(): Promise<string>
```

* Simulate delay (1 second)
* Return `"User data loaded"`

---

#### Exercise 9 (10 pts)

```ts
async function testFlow()
```

Flow:

1. Call `openPage()`
2. Call `fetchUser()`
3. Print results in correct order

---

### 🔹 Section 5: Automation Simulation (20 points)

#### Exercise 10 (20 pts)

```ts
type Credentials = {
  username: string
  password: string
}

async function loginTest(cred: Credentials): Promise<void>
```

Steps:

1. Print `"Opening login page"`
2. Print `"Entering username: <username>"`
3. Print `"Entering password"`
4. Validate password:

   * < 6 → `"Test Failed"`
   * ≥ 6 → `"Test Passed"`

---

## ⭐ Bonus (Optional – up to +10 points)

### Exercise 11 (+5 pts)

Create class:

```ts
class LoginPage {
  open(): void
  login(username: string, password: string): void
}
```

---

### Exercise 12 (+5 pts)

```ts
function wait(seconds: number): Promise<void>
```

* Simulate delay using `setTimeout`

---

## 📊 Scoring Rubric (100 points total)

| Category              | Criteria                                      | Points |
| --------------------- | --------------------------------------------- | ------ |
| Basic Syntax          | Correct types, syntax, output                 | 10     |
| Arrays & Objects      | Proper typing, clean structure                | 20     |
| Control Flow          | Correct logic handling                        | 20     |
| Async/Await           | Proper use of async/await, order of execution | 30     |
| Automation Simulation | Logical flow similar to real test             | 20     |
| Bonus                 | Class + reusable function                     | +10    |

---

## ❌ Common Mistakes (Will Deduct Points)

* Using `any` type unnecessarily (-5)
* Not using `async/await` correctly (-10)
* Hardcoding values without logic (-5)
* Code not runnable (-10)
* Missing README (-5)

---

## ▶️ How to Run

```bash
npm install
npx tsc
node dist/exerciseX.js
```

---

## ✅ Acceptance Criteria

You PASS this assignment if:

* Score ≥ 70 points
* Understand async flow
* Can explain your code

---

## 🚀 Next Step

After passing:
👉 Move to **Week 1 – Playwright Basics**
