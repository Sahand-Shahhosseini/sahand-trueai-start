import SwiftUI

struct ContentView: View {
    @State private var numbersText: String = "0.1,0.2,0.3"
    @State private var result: String = ""

    var body: some View {
        NavigationView {
            VStack(spacing: 20) {
                TextField("Enter numbers", text: $numbersText)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding()

                Button("Compute Fractal") {
                    Task {
                        await computeFractal()
                    }
                }
                .buttonStyle(.borderedProminent)

                Text(result)
                    .padding()
            }
            .navigationTitle("Sahand Fractal")
        }
    }

    func computeFractal() async {
        let numbers = numbersText.split(separator: ",").compactMap { Double($0.trimmingCharacters(in: .whitespaces)) }
        guard let url = URL(string: "http://localhost:8000/fractal") else { return }
        do {
            var request = URLRequest(url: url)
            request.httpMethod = "POST"
            let payload = ["numbers": numbers]
            request.httpBody = try JSONSerialization.data(withJSONObject: payload)
            request.addValue("application/json", forHTTPHeaderField: "Content-Type")
            let (data, _) = try await URLSession.shared.data(for: request)
            if let json = try JSONSerialization.jsonObject(with: data) as? [String: Any],
               let res = json["result"] {
                result = String(describing: res)
            }
        } catch {
            result = "Error: \(error.localizedDescription)"
        }
    }
}

#Preview {
    ContentView()
}
