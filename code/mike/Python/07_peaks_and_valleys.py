# peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.
# valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
# peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(elevations):
    peak_indices = []
    for p in range(1,len(elevations)-1):
        previous = elevations[p-1]
        current = elevations[p]
        next = elevations[p+1]
        if previous < current and next < current:
            peak_indices.append(p)
    return peak_indices

found_peaks = peaks(data)
print(peaks(data))

def valleys(lows):
    valleys_indices = []
    for v in range(1,len(lows)-1):
        previous = lows[v-1]
        current = lows[v]
        next = lows[v+1]
        if previous > current and next > current:
            valleys_indices.append(v)
    return valleys_indices

found_valleys = valleys(data)
print(valleys(data))

def peaks_valleys(peaks, valleys):
        return sorted(peaks + valleys)

print(peaks_valleys(data))

def main():
	data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
	print(peaks(data))
	print(valleys(data))
	print(peaks_valleys(data))

