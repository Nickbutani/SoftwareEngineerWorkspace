function createFrequencyCounter(arr) {
  return arr.reduce((acc, curr) => {
    acc[curr] = (acc[curr] || 0) + 1;
    return acc;
  }, {});
}

function findMean(nums) {
    if (nums.length === 0) return 0;
    return nums.reduce((acc, curr) => acc + curr) / nums.length;
}

function findMedian(nums) {
    nums.sort((a, b) => a - b);
    let middleIndex = Math.floor(nums.length / 2);
    let median;
    if (nums.length % 2 === 0) {
        median = (nums[middleIndex - 1] + nums[middleIndex]) / 2;
    } else {
        median = nums[middleIndex];
    }
    return median;
}

function findMode(nums) {
    let freqCounter = createFrequencyCounter(nums);
    let count = 0;
    let mostFrequent;
    for (let key in freqCounter) {
        if (freqCounter[key] > count) {
            mostFrequent = key;
            count = freqCounter[key];
        }
    }
    return mostFrequent;
}

function convertAndValidateNumsArray(numsAsStrings) {
    let result = [];

    for (let i = 0; i < numsAsStrings.length; i++) {
      let valToNumber = Number(numsAsStrings[i]);
  
      if (Number.isNaN(valToNumber)) {
        return new Error(
          `The value '${numsAsStrings[i]}' at index ${i} is not a valid number.`
        );
      }
  
      result.push(valToNumber);
    }
    return result;
}

module.exports = {
    createFrequencyCounter,
    findMean,
    findMedian,
    findMode,
    convertAndValidateNumsArray
};

