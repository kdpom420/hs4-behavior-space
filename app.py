import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="HS4 Behavioral State Space",
    layout="wide"
)

@st.cache_data
def load_data():
    hs = pd.read_csv("data/hs_ai_cluster_rank_final.csv")
    year = pd.read_csv("data/hs_year_feature_umap.csv")
    drift = pd.read_csv("data/hs_drift_ranking.csv")
    return hs, year, drift

hs, year, drift = load_data()

st.title("Behavioral State Space Analysis of HS4 Trade Goods")
st.caption("South Korea HS4 export data, UN Comtrade, 2018–2024")

st.markdown("""
This app explores HS4 trade goods as behavioral state vectors for identifying
international postal-friendly HS goods.  
Only derived analysis files are used. Raw UN Comtrade data is not included.
""")

tab1, tab2, tab3 = st.tabs([
    "HS Behavioral Space",
    "Postal-Friendly Ranking",
    "Topology Drift"
])

with tab1:
    st.subheader("UMAP Behavioral Space")

    cluster_filter = st.multiselect(
        "Select clusters",
        sorted(hs["cluster"].unique()),
        default=sorted(hs["cluster"].unique())
    )

    view = hs[hs["cluster"].isin(cluster_filter)]

    fig = px.scatter(
        view,
        x="UMAP1",
        y="UMAP2",
        color="cluster",
        hover_name="cmdCode_clean",
        hover_data=[
            "hs_desc",
            "postal_hs_score",
            "recent_growth",
            "growth_persistence",
            "country_diversity"
        ],
        text="cmdCode_clean",
        title="HS4 Behavioral State Space"
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("International Postal-Friendly HS Code Candidates")

    top_n = st.slider("Top N", 5, 50, 20)

    rank = hs.sort_values(
        "postal_hs_score",
        ascending=False
    ).head(top_n)

    st.dataframe(
        rank[[
            "cmdCode_clean",
            "hs_desc",
            "cluster",
            "postal_hs_score",
            "recent_growth",
            "growth_persistence",
            "country_diversity",
            "volatility"
        ]],
        use_container_width=True
    )

    fig2 = px.bar(
        rank.sort_values("postal_hs_score"),
        x="postal_hs_score",
        y="cmdCode_clean",
        orientation="h",
        hover_data=["hs_desc"],
        title="Postal-Friendly HS Score"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    st.subheader("Postal-Friendly Goods Similarity Tree")

    feature_cols = [
        "recent_growth",
        "growth_persistence",
        "country_diversity",
        "volatility"
    ]

    top_n_tree = st.slider("Dendrogram Top N", 10, 40, 25)

    tree_df = (
        hs.sort_values("postal_hs_score", ascending=False)
          .head(top_n_tree)
          .copy()
    )

    tree_df = tree_df.dropna(subset=feature_cols)

    if len(tree_df) < 2:
        st.warning("Dendrogram requires at least two HS codes after removing missing values.")
    else:
        X = tree_df[feature_cols].values
        X_scaled = StandardScaler().fit_transform(X)

        labels = (
            tree_df["cmdCode_clean"].astype(str)
            + " "
            + tree_df["hs_desc"].astype(str).str[:25]
        )

        Z = linkage(X_scaled, method="ward")

        fig_tree, ax = plt.subplots(figsize=(10, max(5, len(tree_df) * 0.35)))
        dendrogram(
            Z,
            labels=labels.tolist(),
            orientation="right",
            leaf_font_size=9,
            ax=ax
        )
        ax.set_title("Similarity Tree of Postal-Friendly Trade Goods")
        ax.set_xlabel("Behavioral Feature Distance")
        st.caption(
            "Hierarchical clustering of HS goods using behavioral trade features."
        )
        fig_tree.tight_layout()
        st.pyplot(fig_tree)
        plt.close(fig_tree)

with tab3:
    st.subheader("HS Topology Drift")

    drift_view = drift.sort_values(
        "drift_length",
        ascending=False
    ).head(30)

    st.dataframe(drift_view, use_container_width=True)

    fig3 = px.bar(
        drift_view.sort_values("drift_length"),
        x="drift_length",
        y="cmdCode_clean",
        orientation="h",
        hover_data=["hs_desc"],
        title="Top HS Codes by Drift Length"
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    target = st.selectbox(
        "Select HS code trajectory",
        sorted(year["cmdCode"].astype(str).unique())
    )

    target_df = year[
        year["cmdCode"].astype(str) == str(target)
    ].sort_values("refYear")

    fig4 = px.line(
        target_df,
        x="UMAP1",
        y="UMAP2",
        markers=True,
        text="refYear",
        title=f"Topology Drift Trajectory: HS {target}"
    )
    fig4.update_traces(textposition="top center")
    st.plotly_chart(fig4, use_container_width=True)

st.divider()

st.markdown("""
### Notes

- This is an exploratory analysis.
- UMAP distance and clustering should not be interpreted as causal evidence.
- Drift may include effects from HS revision, reporting differences, and data noise.
- Raw UN Comtrade data is not distributed in this app.
""")
