from math import trunc
from matplotlib.pyplot import bar, xlabel, ylabel, show, grid

def get_buckets(values, step):
    min_value = trunc(min(values))
    max_value = trunc(max(values))
    return list(range(min_value, max_value, step))

def get_closest_bucket(value, buckets):
    closest_bucket = buckets[0]
    for bucket in buckets:
        if abs(value - closest_bucket) > abs(value - bucket):
            closest_bucket = bucket
    return closest_bucket

def sort_into_buckets(values, buckets):
    buckets_to_values = {key:[] for key in buckets}
    step = buckets[1] - buckets[0]
    for value in values:
        buckets_to_values[get_closest_bucket(value, buckets)].append(value)
    return buckets_to_values

def get_histogram_data(buckets_to_values):
    return {bucket: len(values) for bucket, values in buckets_to_values.items()}

def draw_histogram(histogram_data):
    grid(True)
    xlabel('Waiting times')
    ylabel('Number of customers')
    bar(histogram_data.keys(), histogram_data.values())
    show()

def main():
    wait_times = [43.1, 35.6, 37.6, 36.5, 45.3, 43.5, 40.3, 50.2, 47.3, 31.2, 42.2, 45.5, 30.3, 31.4, 35.6, 45.2, 54.1, 45.6, 36.5, 43.1]
    step = 5
    buckets = get_buckets(wait_times, step)
    buckets_to_values = sort_into_buckets(wait_times, buckets)
    histogram_data = get_histogram_data(buckets_to_values)
    draw_histogram(histogram_data)

if __name__ == "__main__":
    main()
