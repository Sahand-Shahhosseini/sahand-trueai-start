import SwiftUI

struct ContentView: View {
    @State private var numbersText: String = "0.1,0.2,0.3"
    @State private var result: [Double] = []
    @State private var isLoading: Bool = false

    var body: some View {
        VStack(spacing: 20) {
            TextField("Enter numbers", text: $numbersText)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            Button("Compute Fractal") {
                Task { await computeFractal() }
            }
            .buttonStyle(.borderedProminent)
            .disabled(isLoading)

            if isLoading {
                ProgressView()
            } else if !result.isEmpty {
                VStack(alignment: .leading) {
                    Text("Results:").font(.headline)
                    ForEach(result.indices, id: \ .self) { idx in
                        Text("\(idx + 1). \(result[idx])")
                    }
                    Divider()
                    let avg = result.reduce(0,+)/Double(result.count)
                    Text("Average: \(avg)")
                }
                .padding()
            }
        }
        .navigationTitle("Sahand Fractal")
    }

    private func computeFractal() async {
        let numbers = numbersText.split(separator: ",").compactMap { Double($0.trimmingCharacters(in: .whitespaces)) }
        guard let url = URL(string: "http://localhost:8000/fractal") else { return }
        isLoading = true
        defer { isLoading = false }
        do {
            var request = URLRequest(url: url)
            request.httpMethod = "POST"
            let payload = ["numbers": numbers]
            request.httpBody = try JSONSerialization.data(withJSONObject: payload)
            request.addValue("application/json", forHTTPHeaderField: "Content-Type")
            let (data, _) = try await URLSession.shared.data(for: request)
            if let json = try JSONSerialization.jsonObject(with: data) as? [String: Any],
               let res = json["result"] as? [Double] {
                result = res
            }
        } catch {
            print("Request error: \(error)")
        }
    }
}

#Preview {
    NavigationView {
        ContentView()
    }
}
