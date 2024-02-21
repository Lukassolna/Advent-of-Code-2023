class Range:
    @staticmethod
    def empty():
        """Returns an empty sequence."""
        return []

    @staticmethod
    def range(from_val, to_val):
        """Creates a sequence with a single range."""
        return [(from_val, to_val)]

    @staticmethod
    def union(*sequences):
        """Unions multiple sequences."""
        seq = []
        for sequence in sequences:
            if sequence is not None:
                seq.extend(sequence)
        return Range._merge_overlapping_ranges(sorted(seq, key=lambda x: x[0]))

    @staticmethod
    def _merge_overlapping_ranges(ranges):
        """Merges overlapping ranges."""
        merged = []
        for current in ranges:
            if not merged:
                merged.append(current)
            else:
                prev_from, prev_to = merged[-1]
                curr_from, curr_to = current
                if curr_from <= prev_to + 1:
                    merged[-1] = (prev_from, max(prev_to, curr_to))
                else:
                    merged.append(current)
        return merged

    @staticmethod
    def intersection(seq1, seq2):
        """Returns the intersection of two sequences."""
        result = []
        for from1, to1 in seq1:
            for from2, to2 in seq2:
                overlap_start = max(from1, from2)
                overlap_end = min(to1, to2)
                if overlap_start <= overlap_end:
                    result.append((overlap_start, overlap_end))
        return result

    @staticmethod
    def difference(seq1, seq2):
        """Returns the difference of two sequences."""
        result = []
        for from1, to1 in seq1:
            adjusted_range = Range._reduce_range((from1, to1), seq2)
            result.extend(adjusted_range)
        return result

    @staticmethod
    def _reduce_range(range_val, seq):
       
        if not seq:
            return [range_val]
        result = []
        from_val, to_val = range_val
        for from2, to2 in seq:
            if to_val < from2 or from_val > to2:
                continue
            if from_val < from2:
                result.append((from_val, from2 - 1))
            if to_val > to2:
                from_val = to2 + 1
            else:
                return result
        if from_val <= to_val:
            result.append((from_val, to_val))
        return result

    @staticmethod
    def add(seq, n):
        """Increments each range in the sequence by n."""
        return [(from_val + n, to_val + n) for from_val, to_val in seq]
