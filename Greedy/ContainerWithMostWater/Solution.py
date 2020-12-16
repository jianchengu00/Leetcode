class Solution:
    def max_area(self, height: list) -> int:
        i = 0
        j = len(height) - 1
        max_water = -1

        while i < j:
            if (j - i) * min(height[i], height[j]) > max_water:
                max_water = (j - i) * min(height[i], height[j])

            # Select the shorter side's neighbor
            # Since the water area is dependent on the smaller side,
            # if we select the taller side's neighbor, we cannot get an increase
            # in area, as we are limited by the smaller of the two sides
            # Thus, we have to go with the smaller one, as only that would
            # have potential to increase the overall area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_water
