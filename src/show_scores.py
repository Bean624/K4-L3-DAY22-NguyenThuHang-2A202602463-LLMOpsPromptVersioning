import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open("evidence/03_ragas_report.json", "r", encoding="utf-8") as f:
    data = json.load(f)

v1 = data["prompt_v1_scores"]
v2 = data["prompt_v2_scores"]

print("=" * 65)
print(f"  {'Metric':30s}  {'V1':>8}  {'V2':>8}  Winner")
print("=" * 65)
for metric in ["faithfulness", "answer_relevancy", "context_recall", "context_precision"]:
    s1, s2 = v1[metric], v2[metric]
    s1_str = f"{s1:>8.4f}" if str(s1) != "nan" else "     nan"
    s2_str = f"{s2:>8.4f}" if str(s2) != "nan" else "     nan"
    s1_val = s1 if str(s1) != "nan" else 0
    s2_val = s2 if str(s2) != "nan" else 0
    winner = "← V1" if s1_val > s2_val else "← V2"
    print(f"  {metric:30s}  {s1_str}  {s2_str}  {winner}")

best_faith = max(v1["faithfulness"], v2["faithfulness"])
print(f"\n✅ Đạt mục tiêu: faithfulness = {best_faith:.4f} ≥ 0.8\n")
