import SwiftUI

@main
struct SahandApp: App {
    var body: some Scene {
        WindowGroup {
            TabView {
                NavigationView { ContentView() }
                    .tabItem {
                        Label("Fractal", systemImage: "circle.grid.cross")
                    }
                NavigationView { LemmaSelectionView() }
                    .tabItem {
                        Label("Lemmas", systemImage: "list.bullet")
                    }
            }
        }
    }
}
