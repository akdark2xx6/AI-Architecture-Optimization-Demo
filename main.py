import time

# === VERSION A: CODE CHƯA TỐI ƯU (Baseline) ===
# Đặc điểm: Dùng vòng lặp lồng nhau O(n^2), logic rối rắm
def version_a_search(data_list, targets):
    results = []
    for target in targets:
        found = False
        for item in data_list: # Vòng lặp lồng nhau cực chậm
            if item == target:
                results.append(item)
                found = True
                break
    return results

# === VERSION B: CODE ĐÃ TỐI ƯU BỞI AI (Optimized) ===
# Đặc điểm: Dùng Hash Map (Set) O(n), logic gãy gọn
def version_b_search(data_list, targets):
    data_set = set(data_list) # Chuyển sang Set để tìm kiếm O(1)
    return [target for target in targets if target in data_set]

# --- Bộ công cụ chạy thử nghiệm ---
data = list(range(10000))
targets = list(range(5000, 7000))

print("🚀 Đang chạy Test Version A...")
start = time.time()
version_a_search(data, targets)
print(f"⏱ Version A mất: {time.time() - start:.4f} giây")

print("\n🚀 Đang chạy Test Version B...")
start = time.time()
version_b_search(data, targets)
print(f"⏱ Version B mất: {time.time() - start:.4f} giây")
