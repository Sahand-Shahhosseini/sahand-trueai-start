from .sahand_sat import SahandSAT


class SahandKnapsack:
    def __init__(self, problem_json):
        self.problem_json = problem_json
        self.sat_solver = SahandSAT()
        self.sat_solver.load_from_json(problem_json)

    def analyze_and_optimize(self, verbose=False):
        self.sat_solver.print_summary()
        solution = self.sat_solver.solve(verbose=verbose)
        self.solution = solution
        return {
            "selected_variables": [
                v for v, val in solution["assignment"].items() if val
            ],
            "total_weight": solution["min_weight"],
            "time": solution["time_seconds"],
        }

    def export_analysis(self, filepath):
        self.sat_solver.export_to_json(filepath, include_solution=True)
