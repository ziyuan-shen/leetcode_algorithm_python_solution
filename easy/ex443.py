class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        while idx < len(chars):
            current_elem = chars[idx]
            idx += 1
            count = 1
            while idx < len(chars) and chars[idx] == current_elem:
                del chars[idx]
                count += 1
            if count > 1:
                for char in str(count):
                    chars.insert(idx, char)
                    idx += 1
        return len(chars)