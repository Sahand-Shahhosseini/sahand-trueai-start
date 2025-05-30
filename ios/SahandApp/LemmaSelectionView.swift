import SwiftUI

struct Lemma: Identifiable, Codable {
    let code: String
    let title: String
    var id: String { code }
}

struct LemmaSelectionView: View {
    @State private var lemmas: [Lemma] = []
    @State private var selectedCodes: Set<String> = []
    @State private var result: [Double] = []
    @State private var isLoading: Bool = false

    var body: some View {
        VStack {
            if lemmas.isEmpty {
                ProgressView().onAppear(perform: loadLemmas)
            } else {
                List(lemmas) { lemma in
                    HStack {
                        Text(lemma.title)
                        Spacer()
                        if selectedCodes.contains(lemma.code) {
                            Image(systemName: "checkmark")
                        }
                    }
                    .contentShape(Rectangle())
                    .onTapGesture {
                        if selectedCodes.contains(lemma.code) {
                            selectedCodes.remove(lemma.code)
                        } else {
                            selectedCodes.insert(lemma.code)
                        }
                    }
                }
                .listStyle(.plain)

                Button("Compute Lemma Fractal") {
                    Task { await computeLemmaFractal() }
                }
                .buttonStyle(.borderedProminent)
                .disabled(selectedCodes.isEmpty || isLoading)

                if isLoading {
                    ProgressView()
                } else if !result.isEmpty {
                    VStack(alignment: .leading) {
                        Text("Results:").font(.headline)
                        ForEach(result.indices, id: \ .self) { idx in
                            Text("\(idx + 1). \(result[idx])")
                        }
                    }
                    .padding()
                }
            }
        }
        .navigationTitle("Lemmas")
    }

    private func loadLemmas() {
        guard let url = Bundle.main.url(forResource: "lemmas", withExtension: "json") else {
            return
        }
        do {
            let data = try Data(contentsOf: url)
            lemmas = try JSONDecoder().decode([Lemma].self, from: data)
        } catch {
            print("Failed to load lemmas: \(error)")
        }
    }

    private func computeLemmaFractal() async {
        guard let url = URL(string: "http://localhost:8000/lemma-fractal") else { return }
        isLoading = true
        defer { isLoading = false }
        do {
            var request = URLRequest(url: url)
            request.httpMethod = "POST"
            let payload = ["codes": Array(selectedCodes)]
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
        LemmaSelectionView()
    }
}
