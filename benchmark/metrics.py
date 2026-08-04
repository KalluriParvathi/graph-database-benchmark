import statistics

def calculate_metrics(times):
    times = sorted(times)

    return {
        "average": round(statistics.mean(times), 3),
        "p50": round(statistics.median(times), 3),
        "p95": round(times[int(len(times) * 0.95)], 3)
    }