public class Exp1 {

     public static int countBigrams(String[] corpus, String word1, String word2) {
        int count = 0;
        for (String sentence : corpus) {
            String[] words = sentence.split(" ");
            for (int i = 0; i < words.length - 1; i++) {
                if (word1.equalsIgnoreCase(words[i]) && word2.equalsIgnoreCase(words[i + 1])) {
                    count++;
                }
            }
        }
        return count;
    }

    public static int countUnigrams(String[] corpus, String word) {
        int count = 0;
        for (String sentence : corpus) {
            for (String w : sentence.split(" ")) {
                if (word.equalsIgnoreCase(w)) {
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String[] corpus = {
                "There is a big garden",
                "Children play in a garden",
                "They play inside beautiful garden"
        };
        String[] testWords = "They play in a big Garden".split(" ");
        double probability = 1;
        int corpusSize = 9;

        for (int i = 0; i < testWords.length - 1; i++) {
            probability *= (double) countBigrams(corpus, testWords[i], testWords[i + 1])
                    / (countUnigrams(corpus, testWords[i]) + corpusSize);
        }

        System.out.printf("Probability: %.8f%n", probability);
    }
}