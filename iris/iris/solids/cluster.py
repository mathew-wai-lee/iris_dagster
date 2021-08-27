from dagster import solid
from dagster import AssetMaterialization, Output, EventMetadata
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

@solid
def create_df(context):
    df = pd.DataFrame(load_iris().data, columns=load_iris().feature_names)
    context.log.info(f"\n{df.describe()}")
    return df


@solid
def normalize_df(context, df):
    normalized_df = pd.DataFrame(normalize(df), columns=df.columns)
    context.log.info(f"\n{normalized_df.describe()}")
    return normalized_df

@solid
def pca_df(context, normalized_df):
    pca = PCA(n_components=4)
    pca_normalized_df = pd.DataFrame(pca.fit_transform(normalized_df))
    context.log.info(f"\n{pca_normalized_df.head()}")

    remote_storage_path = "./"
    pca_normalized_df.to_csv(remote_storage_path + "pca.csv")

    yield AssetMaterialization(
        asset_key="pca_csv",
        description="PCA to csv",
        metadata={
            "row_count": EventMetadata.int(int(pca_normalized_df.count()[0])),
        },
    )

    yield Output([pca_normalized_df, pca])

@solid
def sse_plot(context, pca_output):
    context.log.info(f"{pca_output[0]}")
    context.log.info(f"{pca_output[1]}")

