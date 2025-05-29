# Cross-Platform Guide

This document explains how to run the **Sahand True AI** backend and example clients on different platforms.

## Windows

1. Install **Python 3.10** or higher from [python.org](https://www.python.org/downloads/windows/).
2. Clone the repository and install dependencies:
   ```cmd
   git clone <repo-url>
   cd sahand-trueai-start
   pip install poetry
   poetry install
   ```
3. Run the FastAPI server:
   ```cmd
   poetry run uvicorn sstai.api.routes:app --reload
   ```
   The API will be available at `http://localhost:8000`.

## .NET Integration

You can call the API from any .NET application using `HttpClient`:

```csharp
var client = new HttpClient();
var payload = new { numbers = new[] { 0.1, 0.2, 0.3 } };
var response = await client.PostAsJsonAsync("http://localhost:8000/fractal", payload);
var result = await response.Content.ReadFromJsonAsync<FractalResponse>();
```

Define `FractalResponse` with a `result` list property. This works on Windows, Linux, and macOS.

## Android Example

The backend can also be consumed from Android apps. Below is a minimal Kotlin snippet using `OkHttp`:

```kotlin
val client = OkHttpClient()
val json = "{"numbers":[0.1,0.2,0.3]}".toRequestBody("application/json".toMediaType())
val request = Request.Builder()
    .url("http://10.0.2.2:8000/fractal")
    .post(json)
    .build()
client.newCall(request).enqueue(object : Callback {
    override fun onResponse(call: Call, response: Response) {
        val body = response.body?.string()
        // parse JSON and update UI
    }
    override fun onFailure(call: Call, e: IOException) { }
})
```

When running on the Android emulator, use `10.0.2.2` to reach the host machine.

## Notes

- The FastAPI backend runs equally on Windows, Linux, and macOS.
- Ensure the backend is accessible on the network for mobile devices.
- You can adapt the example code to any framework (Flutter, React Native, etc.) as long as it can make HTTP requests.
