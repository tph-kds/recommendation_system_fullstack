<h1 align="center">RECOMMENDATION SYSTEM FULLSTACK PROJECT</h1>
<p align="center">
  <img align="center" src="https://github.com/tph-kds/image_storages/blob/d88caf2b45c0ef2eeee160608205344706c5f938/images/svgs/recommendation_system/logo_bg.png" width="800">
  
</p>

# Contents
* [Introduce](#i-introduce)
    * [The goals of project](#1-the-goals-of-project)
    * [Data Sources](#2-data-sources)
    * [Steps of project](#3-steps-of-project)
    * [Deployment](#4-deployment-for-this-project)
    * [Data Lineage](#5-data-lineage-projects-workflow)
* [Getting Started](#ii-getting-started)
* [Algorithms](#iii-algorithms)
    * [Algorithm Comparison](#algorithm-comparison)
* [References](#iv-references)


## I. Introduce

### 1. The goals of project
Studying and developing for the real-life project with recommendation system topic use integrated continous pipeline. Moreover, its application will deploy into the social media such as website and help some people approach closely about boardgame.   


### 2. Data Sources
Datasets are taken from link > https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews/
But `Boardgame Reviewer` datasets are originally extracted by `BoardgameGeek` website. - one of the popular games' information website around the world.


> **BoardgameGeek:**
>
Link website: https://boardgamegeek.com/

### 3. Steps of project
Boardgame recommendation systems is to assist researchers, developers and enthusiasts in prototyping, experimenting with and bringing to production a range of classic and state-of-the-art recommendation systems about thinking game model.



This repository contains examples and best practices for building recommendation systems, provided as Jupyter notebooks, between some folders and used methods. The examples detail our learnings on five key tasks:

- [Prepare Data](Test): Preparing and loading data for each recommendation algorithm.
- [Model](Test): Building models using various classical and recommendation algorithms such as Collaborative Filtering Based ([CFB](https://medium.com/@evelyn.eve.9512/collaborative-filtering-in-recommender-system-an-overview-38dfa8462b61)) and Content Based ([CB](https://developers.google.com/machine-learning/recommendation/content-based/basics)) Hybrid RS ([HRS](https://www.kaggle.com/code/iambideniz/hybrid-recommender-system)) and Merge Average Based RS ([MAB](https://www.kaggle.com/code/iambideniz/hybrid-recommender-system)).
- [Evaluate](test): Evaluating algorithms with offline metrics.
- [Model Select and Optimize](test): Fine tuning and optimizing hyperparameters for recommendation models.
- [Deployment](app): Deployment models in a production environment on Website by using ([Flask Framework](https://flask.palletsprojects.com/en/3.0.x/)).

Several utilities are provided in [src](src) to support common tasks such as complete seperate stages and algorithmns and combine them to receive a accuracy and confident result throughout [src/Hydrid RS](src/Hybrid_RS/) . See the detailly processing stream and workflow of all project, you can run at [main.py](src/main.py).

For a more detailed overview of the repository, please see the documents on the [github page](https://github.com/tph-kds/recommendation_system_fullstack).


### 4. Deployment for this project
<p align="center">
  <img src="https://github.com/tph-kds/image_storages/blob/1bd43f03c9d581bb8660a8709fd95521733fcddf/images/svgs/recommendation_system/deployment.png" width="800">
</p>

For some of the practical deployment where recommendation systems have been applied, see [deployment]().  


### 5. Data Lineage ([Project's Workflow](workflow.png))
<p align="center">
  <img src="https://github.com/tph-kds/image_storages/blob/d8747de52fee64e0091f1152f928688ef9d90bda/images/svgs/recommendation_system/data_lineage.png" width="800">
</p>

## II. Getting Started

We recommend [conda](https://docs.conda.io/projects/conda/en/latest/glossary.html?highlight=environment#conda-environment) for environment management, and [VS Code](https://code.visualstudio.com/) for development. To install the recommendation system about boardgames topic package and run an example notebook on Linux/WSL:

```bash
# 1. Install gcc if it is not installed already. On Ubuntu, this could done by using the command
# sudo apt install gcc

# 2. Create and activate a new conda environment
conda create -n <environment_name> python=3.9
conda activate <environment_name>

# 3. Install the core recommenders package. It can run all the CPU notebooks.
pip install rs_boardgame

# 4. create a Jupyter kernel
python -m ipykernel install --user --name <environment_name> --display-name <kernel_name>

# 5. Clone this repo within VSCode or using command line:
git clone https://github.com/tph-kds/recommendation_system_fullstack

# 6. Within VSCode:
#   a. Open a notebook, e.g., examples/00_quick_start/sar_movielens.ipynb;  
#   b. Select Jupyter kernel <kernel_name>;
#   c. Run the notebook.
```

For more information about setup on other platforms (e.g., Windows and macOS) and different configurations, see the [Setup Guide](https://gist.github.com/alexwolson/9cfbb9e5312808cce9d730eb577e18f3).


## III. Algorithms

The table below lists the recommendation algorithms currently available in the repository. Notebooks are linked under the Example column as Quick start, showcasing an easy to run example of the algorithm, or as Deep dive, explaining in detail the math and implementation of the algorithm.

| Algorithm | Type | Description | Example |
|-----------|------|-------------|---------|
| Similarity Based Recommendation Systems (SBRS) | Collaborative Filtering | It relies on the similarity value between items to make recommendations. The system calculates how similar items are to each other based on user interactions, such as ratings, views, or purchases. When a user interacts with an item, the system recommends other items that are similar based on these calculated similarities. This approach is particularly useful for generating recommendations when there is a large number of users and the focus is on the relationships between items rather than users." This description focuses on the key aspects of similarity-based item-item recommendation systems, without conflating it with other techniques like matrix factorization. It works in the CPU/GPU environment.| [Quick start](Test/Collaborative_Filtering) |
| Similarity Based Recommendation Systems (SBRS) | Content Based Filtering | Content-based filtering is another popular recommendation technique that, like item-item collaborative filtering, relies on similarity. However, instead of using the similarity between items based on user interactions, content-based filtering uses the attributes or features of the items themselves. It works in the CPU/GPU environment. | [Quick start](Test/Content_Based) |
| Weight-rating<sup>*</sup> | Hydrid Based | Weight-rating methods are used to aim to enhance the accuracy of the recommendations by assigning different weights to items or features based on their importance or relevance. It works in the CPU/GPU environment. | [Quick start](Test/Hybrid) |
| Mergetive Result Average<sup>*</sup> | Merge Average Based |  Mergetive Result Average algorithm that aims to capture and merge all of method results throughout averaging between the weights represents the mutual importance of the results - 3 methods which are used above. These weights can be adjusted during fine tuning processing. It works in the CPU/GPU environment. | [Quick start](Test/Hybrid) |



### Algorithm Comparison

I provide a benchmark notebook to illustrate how different algorithms could be evaluated and compared. In this notebook, the project's dataset is split into training/test sets at a 75/25 ratio using a stratified split. A recommendation model is trained using each of the collaborative filtering algorithms below. We utilize empirical parameter values reported in literature [here](http://mymedialite.net/examples/datasets.html). For ranking metrics we use `k=10` (top 10 recommended items). In this table we show the results on 20,588 boardgame name, running the algorithms for 10 epochs.

| Algo | MAP | Precision@k | Recall@k |
| --- | --- | --- |  --- |
| [CFB](examples/00_quick_start/als_movielens.ipynb) | 0.003428 |	0.012902 | 0.010606 |
| [CB](examples/02_model_collaborative_filtering/cornac_bivae_deep_dive.ipynb) | N/A	|  0.069507 |	0.000491 |
| [HRS](examples/02_model_collaborative_filtering/cornac_bpr_deep_dive.ipynb) | N/A	| N/A | N/A |
| [MAB](examples/02_model_collaborative_filtering/cornac_bpr_deep_dive.ipynb) | 0.100258	|  0.125029 |	0.104856 |


## IV. References

- **FREE COURSE** : M. González-Fierro, "Recommendation Systems: A Practical Introduction", LinkedIn Learning, 2024. [Available on this link](https://www.linkedin.com/learning/recommendation-systems-a-practical-introduction).
- **PAPER** : D. Li, J. Lian, L. Zhang, K. Ren, D. Lu, T. Wu, X. Xie, "Recommender Systems: Frontiers and Practices", Springer, Beijing, 2024. [Available on this link](https://www.amazon.com/Recommender-Systems-Frontiers-Practices-Dongsheng/dp/9819989639/).

- **KAGGLE** : Jesse Van Elteren. Boardgamegeek reviews , 2022.
[Available on this link](https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews/)
[Online; accessed January 8, 2024].

- **GEEK** : Boardgamegeek. [Available on this link](https://boardgamegeek.com/). [Online; accessed January 8, 2024].

- **GITHUB** : Boardgame recommendation system, 2023-2024. [Available on this link](https://github.com/tph-kds/recommendation_system_fullstack.git/)
. [Online; accessed January 8, 2024].

- **NVIDIA** : Recommendation system.
[Available on this link](https://www.nvidia.com/en-us/glossary/data-science/recommendation-system/)
. [Online; accessed January 8, 2024].
