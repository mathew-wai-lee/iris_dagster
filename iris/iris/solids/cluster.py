from dagster import solid
from dagster import AssetMaterialization, Output, EventMetadata
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

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
    yield AssetMaterialization(asset_key="pca_df", description="Wrote PCA df to fs")
    yield Output(remote_storage_path)

    yield EventMetadata.int(100)


    return pca_normalized_df 

