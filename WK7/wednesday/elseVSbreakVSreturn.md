# Differences and Use Cases: `return`, `else`, `break` in Python

---

## `return`
- **What it does:** Immediately exits a function and can return a value.
- **Use case:** When you want to stop the execution of a function before reaching the end, for example, if a special condition or error occurs.
- **Example:**
    ```python
    def f(x):
        if x < 0:
            return "Negative"
        return "Non-negative"
    ```

---

## `break`
- **What it does:** Immediately exits a loop (`for` or `while`), but not the function.
- **Use case:** When you want to stop a loop before it finishes normally, for example, when you find a specific element.
- **Example:**
    ```python
    for i in range(10):
        if i == 5:
            break
        print(i)
    ```

---

## `else` (in if and loops)
- **In if:** Executes if the if condition is false.
    - **Use case:** When you want to run a block of code only if the condition is not met.
    - **Example:**
        ```python
        if x > 0:
            print("Positive")
        else:
            print("Not positive")
        ```
- **In loops:** Executes if the loop finishes normally (not by a break).
    - **Use case:** When you want to execute something only if the loop was not interrupted by a break.
    - **Example:**
        ```python
        for i in range(5):
            if i == 3:
                break
        else:
            print("The loop finished normally")
        ```

---

## Summary

- Use `return` to exit a function.
- Use `break` to exit a loop.
- Use `else` to handle the opposite case of an if, or to execute code after a loop only if there was no break.