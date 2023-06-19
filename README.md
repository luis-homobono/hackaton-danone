➡️ Context:

As one of the world's largest food and beverage companies, Danone is on a mission to produce healthful products while minimizing its environmental footprint. With a vast product line-up, including dairy, plant-based items, water, and specialized nutrition products, the company is constantly innovating to meet global dietary needs. With the increasing focus on sustainability, Danone is aware of the pressing need to evaluate and enhance the ecological footprint of its offerings.

This challenge involves leveraging data science and analytics to identify areas where Danone can reduce its environmental impact across its product lifecycle, from raw ingredient sourcing to manufacturing and distribution. Your goal is to create a machine learning model that accurately classifies Danone's products according to their eco score grade.

📄 Dataset:

For this challenge, you will have 2 JSON files: train_products.json, and test_products.json. As their names indicate, the first one will be used to train your classification model. The test file will be the one where you will use to predict the ecoscore grade with your trained model, to generate the predictions file.

    train_products.json:  Download train_products.json file.
    test_products.json: Download test_products.json file.

You will have the following attributes as values of each id in the json file, to be able to make the classifications:

    name: Name of the product
    brand: name of the brand, or names of the sub-brand and brand
    generic_name: generic product name, if any
    categories_hierarchy: hierarchically ordered list of categories and sub categories for the product
    is_beverage: indicates if the product is a beverage or not
    selling_countries: list of countries where the product is being sold to
    ingredient_origins: dictionary with regions as keys and percentage of ingredients coming from these regions as values.
    ingredients: list of ingredients with their optional attributes, ordered by rank or order of appearance on the packaging label. Each ingredient can have the following subfields:
        has_sub_ingredients: Indicates if the ingredient is a sub-ingredient of the previous full ingredient (the one with the lowest rank found before this sub_ingredient).
        ciqual_food_code: code for the ingredient on the CIQUAL french food composition database.
        id: identifier of the ingredient/ingredient name.
        percent: percentage of the ingredient found on the product, if stated on the packaging.
        percent_estimate: estimation of percentage of the ingredient found on the product. If the percentage is stated on the packaging, then this value is the same as ''percent'.
        percent_max: estimation of maximum percentage of the ingredient found on the product. If the percentage is stated on the packaging, then this value is the same as ''percent'.
        percent_min: estimation of minimum percentage of the ingredient found on the product. If the percentage is stated on the packaging, then this value is the same as ''percent'.
        rank: indicates the order of the ingredient on the packaging label. Higher rank indicates that the ingredient is more present on that product that other ingredients with lower ranks.
        text: text string found on the product packaging label.
        vegan: indicates if the ingredient is vegan-friendly.
        vegetarian: indicates if the ingredient is vegetarian-friendly.
    additives_count: number of additive ingredients found on the product.
    calcium_100g: grams of calcium found per 100g of product.
    carbohydrates_100g: grams of carbohydrates found per 100g of product.
    energy_kcal_100g: kcal of energy obtained per 100g of product.
    fat_100g: grams of fat found per 100g of product.
    fiber_100g: grams of fiber found per 100g of product.
    proteins_100g: grams of protein found per 100g of product.
    salt_100g: grams of salt found per 100g of product.
    sodium_100g: grams of sodium found per 100g of product.
    sugars_100g: grams of sugar found per 100g of product.
    nutrition_grade: grade of the nutrition score of the product.
    packaging_materials: list of materials found on the packaging of the product.
    non_recyclable_and_non_biodegradable_materials_count: Number of non recyclable and non biodegradable packaging materials
    est_co2_agriculture: estimated CO2eq emissions generated on the agricultural process needed for creating the product
    est_co2_consumption: estimated CO2eq emissions generated on the consumption process of the product
    est_co2_distribution: estimated CO2eq emissions generated on the product distribution process
    est_co2_packaging: estimated CO2eq emissions generated on the packaging manufacturing process needed for creating the product
    est_co2_processing: estimated CO2eq emissions generated when processing the ingredients to create the product
    est_co2_transportation: estimated CO2eq emissions generated on the product transportation process
    ecoscore_grade: the target value to predict on the test data. It is an '0' - '4' grade that explains the ecological impact of the product, based on a diverse set of variables. '0' means low ecological impact, while '4' means very high ecological impact.

🎯 Objectives and tasks:

    Predicting the ecoscore_grade of Danone products (test data).
    Data preprocessing:

    Processing of the json data to a format with which the model can be trained.
    Extraction of features from the json that are useful for the model.

✍️ Evaluation:

The evaluation and scoring of this challenge will be evaluated using the F1-score macro criteria.

ℹ️ Solution development and delivery:

⚠️ CONDITIONS FOR YOUR SOLUTION TO BE EVALUATED CORRECTLY:

There must be the file predictions.json with your predictions.

Your repository must be public. If you created your repository from VSCode and your top main branch is 'master', you need to create a branch called 'main' and move everything to this branch. If your link ends in '.git' remove the '.git' from the url and paste it.

👍 Correct link: https://github.com/CarlosIbCu/example_se

👎 Incorrect link: https://github.com/CarlosIbCu/example_se.git

You can see an example in: Download template.json file.

- To deliver and upload your solution in NUWE's platform you will have time till Monday, June 19th at 10 am (Mexico CST)- 18 pm (Europe-CEST), but it's important to be on Hackathon Virtual Day in order to have interaction with DANONE mentors, do networking during the day with DANONE Mexico team in the networking space and have direct contact with them.

📍 Virtual World:

We are happy to tell you that the DANONE HACKATHON MEXICO will be held in the Gather virtual world which will allow you to meet a few representatives of DANONE Mexico team. Click HERE to the Gather virtual world.

Before entering the virtual world you should read this guide: DANONE HACKATHON GATHER VIRTUAL GUIDE .