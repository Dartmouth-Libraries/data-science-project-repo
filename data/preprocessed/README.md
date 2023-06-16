# Preprocessed data

Sometimes data needs to be transformed before it is used in further analysis or ingested by models. If these transformations are static (i.e., the parameters of the preprocessing pipeline are fixed), it usually makes sense to store the preprocessed data in files, so that downstream analyses and models do not have to re-run the (potentially costly) preprocessing pipeline.
