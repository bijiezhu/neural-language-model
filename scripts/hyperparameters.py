from os.path import join, expanduser

#: Not actually used directly, just for convenience
DATA_DIR = join(expanduser("~"), "dev/python/language-model/data/")

# Should we induce an embedding for OOV words?
INCLUDE_UNKNOWN_WORD = True

#VOCABULARY_SIZE = 5000
#VOCABULARY_SIZE = 10000
VOCABULARY_SIZE = 50000

RUN_NAME = "english-wikitext.case-intact"
TRAIN_SENTENCES = join(DATA_DIR, "%s.train.txt.gz" % RUN_NAME)
VALIDATION_SENTENCES = join(DATA_DIR, "%s.validation-1000.txt.gz" % RUN_NAME)
VOCABULARY = join(DATA_DIR, "vocabulary-%s-%d.txt.gz" % (RUN_NAME, VOCABULARY_SIZE))
VOCABULARY_IDMAP_FILE = join(DATA_DIR, "idmap.%s-%d.include_unknown=%s.pkl.gz" % (RUN_NAME, VOCABULARY_SIZE, INCLUDE_UNKNOWN_WORD))

NORMALIZE_EMBEDDINGS = False
#NORMALIZE_EMBEDDINGS = True
#UPDATES_PER_NORMALIZE_EMBEDDINGS = 1000

NGRAM_FOR_TRAINING_NOISE = 0

#NGRAMS = {(1, 5000): join(DATA_DIR, "1grams-wikitext-5000.json.gz"),
#(1, 10000): join(DATA_DIR, "1grams-wikitext-10000.json.gz"),
#(1, 20000): join(DATA_DIR, "1grams-wikitext-20000.json.gz")}

# Number of instances of each ngram to add, for smoothing.
TRAINING_NOISE_SMOOTHING_ADDITION = 0

# Each embedded word representation has this width
EMBEDDING_SIZE = 50
#EMBEDDING_SIZE = 5

# Predict with a window of five words at a time
WINDOW_SIZE = 5

HIDDEN_SIZE = 100
#HIDDEN_SIZE = 10

#: Scaling value to control range for weight initialization
#SCALE_INITIAL_WEIGHTS_BY = math.sqrt(3)
SCALE_INITIAL_WEIGHTS_BY = 1

# Which activation function to use?
#ACTIVATION_FUNCTION="sigmoid"
#ACTIVATION_FUNCTION="tanh"
ACTIVATION_FUNCTION="softsign"

#LEARNING_RATE = 0.001
#LEARNING_RATE = 0.01
LEARNING_RATE = 0.1

# The learning rate for the embeddings
EMBEDDING_LEARNING_RATE = 0.1

## number of (higher-order) quadratic filters for James's neuron
#NUMBER_OF_QUADRATIC_FILTERS=0
## We use this scaling factor for initial weights of quadratic filters,
## instead of SCALE_INITIAL_WEIGHTS_BY
## @note: Try between 10 and 0.01
#SCALE_QUADRATIC_INITIAL_WEIGHTS_BY = 1

# Validate after this many examples
VALIDATE_EVERY = 10000000
#VALIDATE_EVERY = 1000
