# M-Pesa STK Push Simulator

A lightweight Python command-line utility that simulates M-Pesa STK Push payment requests. It validates Kenyan phone numbers and transaction amounts, generates unique transaction references, and simulates network responses with automatic retry logic.

## Features

* **Phone Number Normalization:** Validates local (`07...` / `01...`) and international (`2547...` / `2541...`) Kenyan mobile numbers and standardizes them to the `254XXXXXXXXX` format.
* **Amount Validation:** Ensures transaction amounts are whole integers within the standard KSH 1 to KSH 150,000 limit.
* **Reference Generation:** Automatically creates a unique 6-digit transaction reference prefixed with `TXN` (e.g., `TXN482910`).
* **Network & Retry Simulation:** Simulates real-world network conditions with a 60% success rate, 30% timeout rate, and 10% insufficient funds rate. Automatically retries up to 3 times on timeouts while halting immediately on insufficient funds.

## Prerequisites

* Python 3.8 or higher (uses assignment expressions / walrus operator `:=`).
* No external third-party libraries required (uses Python standard libraries: `random`, `sys`, `re`).

## Installation

1. Clone the repository or download `stk.py`:
   ```bash
   git clone https://github.com
   cd stk-push-simulator
   ```

## Usage

Run the script from your terminal by passing the recipient's phone number and the amount as command-line arguments:

```bash
python stk.py <PHONE> <AMOUNT>
```

### Arguments

| Argument | Description | Accepted Formats |
| :--- | :--- | :--- |
| `PHONE` | Kenyan mobile phone number. | `07XXXXXXXX`, `01XXXXXXXX`, `2547XXXXXXXX`, `2541XXXXXXXX` |
| `AMOUNT` | Transaction amount in KSH. | Whole numbers from `1` to `150000` |

### Examples

**Valid Transaction:**
```bash
python stk.py 0712345678 500
```

**Sample Output (Success):**
```text
Reference: TXN839201
Attempt 1: success
Sent KSH 500 to 254712345678
```

**Sample Output (Timeout with Retry):**
```text
Reference: TXN194023
Attempt 1: timeout, retrying...
Attempt 2: success
Sent KSH 500 to 254712345678
```

**Sample Output (Insufficient Funds):**
```text
Reference: TXN502918
Attempt 1: insufficient funds
Failed: customer has insufficient funds. No retry.
```

## Error Handling

The program exits immediately with clear feedback if invalid arguments are supplied:
* **Missing or extra arguments:** `Usage: python stk.py PHONE AMOUNT`
* **Invalid phone format:** `Invalid Phone`
* **Out-of-range or non-numeric amount:** `Invalid Amount`
* **Max retries exceeded:** `Failed: no response after 3 attempts. Reference <TXNXXXXXX> - check status before retrying.`
