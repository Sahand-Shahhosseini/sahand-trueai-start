# Sahand iOS App

This folder contains a SwiftUI application that communicates with the `SSTAI` FastAPI backend. It now includes two main views:

- **Fractal** – enter comma separated numbers and compute the fractal values using the `/fractal` endpoint.
- **Lemmas** – browse the 150 Sahand Fractal Lemmas, select any subset and compute fractal values via `/lemma-fractal`.

To run the app, open `SahandApp` in Xcode and build for an iOS simulator or device. Ensure the backend is running locally on port `8000`.
