import streamlit as st
import numpy as np
import pandas as pd
import json
import altair as alt
from pathlib import Path
import requests


class Dashboard:
    class Model:
        pageTitle = "Dashboard"

        wordsTitle = "Words"

        inferenceTimeTitle = "Inference Time"

        documentsTitle = "Documents"

        dailyInferenceTitle = "Top Daily Inference"

        accuracyTitle = "Mean Accuracy"

        titleModelEval = "## Evaluation Accuracy"
        titleInferencePerformance = "## Inference Performance"
        titleDatasetInfo = "## Dataset Info"
        titleDataAnnotation = "## Data Annotation"
        titleTrainingPerformance = "## Training Performance"
        titleEvaluationPerformance = "## Evaluation Performance"

        status_file = "docs/status.json"
        annotation_files_dir = "docs/json"

    def view(self, model):
        # st.title(model.pageTitle)

        # Use mock data when APIs are not available
        json_data_inference = [
            [2.3, {"accuracy": 0.85, "processing_time": 2.3}, "model_v1", "inference_001", "2023-01-01 10:30:00"],
            [2.1, {"accuracy": 0.87, "processing_time": 2.1}, "model_v1", "inference_002", "2023-01-02 11:15:00"],
            [1.9, {"accuracy": 0.89, "processing_time": 1.9}, "model_v2", "inference_003", "2023-01-03 09:45:00"]
        ]
        
        json_data_training = [
            [45, {"loss": 0.45, "epochs": 10}, "model_v1", "training_001", "2023-01-01 14:20:00"],
            [42, {"loss": 0.42, "epochs": 12}, "model_v1", "training_002", "2023-01-02 15:30:00"],
            [38, {"loss": 0.38, "epochs": 15}, "model_v2", "training_003", "2023-01-03 16:10:00"]
        ]
        
        json_data_evaluate = [
            [85, {"mean_accuracy": 0.85, "accuracies": 0.85}, "model_v1", "evaluate_001", "2023-01-01 12:00:00"],
            [87, {"mean_accuracy": 0.87, "accuracies": 0.87}, "model_v1", "evaluate_002", "2023-01-02 13:15:00"],
            [89, {"mean_accuracy": 0.89, "accuracies": 0.89}, "model_v2", "evaluate_003", "2023-01-03 14:30:00"]
        ]

        with st.container():
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                words_count = 0
                delta_words = 0

                if len(json_data_inference) > 3:
                    for i in range(0, len(json_data_inference)):
                        words_count = words_count + json_data_inference[i][1]

                    avg_word_count = words_count / len(json_data_inference)
                    avg_word_last = (json_data_inference[len(json_data_inference) - 1][1]
                                     + json_data_inference[len(json_data_inference) - 2][1] +
                                     json_data_inference[len(json_data_inference) - 3][1]) / 3

                    if avg_word_last >= avg_word_count:
                        delta_words = round(100 - ((avg_word_count * 100) / avg_word_last), 2)
                    else:
                        delta_words = round(100 - ((avg_word_last * 100) / avg_word_count), 2) * -1

                    words_count = words_count / 1000
                st.metric(label=model.wordsTitle, value=str(words_count) + 'K', delta=str(delta_words) + "%")

            with col2:
                docs_count = len(json_data_inference)
                delta_docs = 0

                if docs_count > 3:
                    inference_dates = []
                    for i in range(0, len(json_data_inference)):
                        inference_dates.append(json_data_inference[i][4].split(" ")[0])

                    inference_dates_unique = []
                    for item in inference_dates:
                        if item not in inference_dates_unique:
                            inference_dates_unique.append(item)

                    if len(inference_dates_unique) > 3:
                        inference_dates_dict = {}
                        for i, key in enumerate(inference_dates_unique):
                            inference_dates_dict[key] = [0]

                        for i in range(0, len(json_data_inference)):
                            inference_dates_dict[json_data_inference[i][4].split(" ")[0]][0] = \
                                inference_dates_dict[json_data_inference[i][4].split(" ")[0]][0] + 1

                        # calculate average for values from inference_dates_dict
                        avg_value = 0
                        for key, value in inference_dates_dict.items():
                            avg_value = avg_value + value[0]
                            if len(inference_dates_dict) > 0:
                                avg_value = round(avg_value / len(inference_dates_dict), 2)
                            else:
                                avg_value = 0

                        # calculate average for last 3 values from inference_dates_dict
                        avg_value_last = 0
                        for i in range(1, 4):
                            avg_value_last = avg_value_last + inference_dates_dict[inference_dates_unique[len(inference_dates_unique) - i]][0]
                        avg_value_last = round(avg_value_last / 3, 2)

                        if avg_value_last > avg_value:
                            delta_docs = round(100 - ((avg_value * 100) / avg_value_last), 2)
                        else:
                            delta_docs = round(100 - ((avg_value_last * 100) / avg_value), 2) * -1

                st.metric(label=model.documentsTitle, value=docs_count, delta=str(delta_docs) + "%")

            with col3:
                inference_dates = []
                for i in range(0, len(json_data_inference)):
                    inference_dates.append(json_data_inference[i][4].split(" ")[0])

                inference_dates_unique = []
                for item in inference_dates:
                    if item not in inference_dates_unique:
                        inference_dates_unique.append(item)

                inference_dates_dict = {}
                for i, key in enumerate(inference_dates_unique):
                    inference_dates_dict[key] = [0]

                for i in range(0, len(json_data_inference)):
                    inference_dates_dict[json_data_inference[i][4].split(" ")[0]][0] = \
                        inference_dates_dict[json_data_inference[i][4].split(" ")[0]][0] + 1

                # loop through the dictionary and find the max value
                max_value = 0
                for key, value in inference_dates_dict.items():
                    if value[0] > max_value:
                        max_value = value[0]

                # calculate average for values from inference_dates_dict
                avg_value = 0
                for key, value in inference_dates_dict.items():
                    avg_value = avg_value + value[0]
                if len(inference_dates_dict) > 0:
                    avg_value = round(avg_value / len(inference_dates_dict), 2)
                else:
                    avg_value = 0

                if max_value > 0:
                    avg_delta = round(100 - ((avg_value * 100) / max_value), 2)
                else:
                    avg_delta = 0

                st.metric(label=model.dailyInferenceTitle, value=max_value, delta=str(avg_delta) + "%")

            with col4:
                inference_time_avg = 0

                # calculate inference time average
                for i in range(0, len(json_data_inference)):
                    inference_time_avg = inference_time_avg + json_data_inference[i][0]
                if len(json_data_inference) > 0:
                    inference_time_avg = round(inference_time_avg / len(json_data_inference), 2)
                else:
                    inference_time_avg = 0

                delta_time = 0
                if len(json_data_inference) > 3:
                    avg_time_last = (json_data_inference[len(json_data_inference) - 1][0] +
                                     json_data_inference[len(json_data_inference) - 2][0] +
                                     json_data_inference[len(json_data_inference) - 3][0]) / 3

                    if avg_time_last > inference_time_avg:
                        delta_time = round(100 - ((inference_time_avg * 100) / avg_time_last), 2)
                    else:
                        delta_time = round(100 - ((avg_time_last * 100) / inference_time_avg), 2) * -1

                st.metric(label=model.inferenceTimeTitle, value=str(inference_time_avg) + " s", delta=str(delta_time) + "%",
                          delta_color="inverse")

            with col5:
                models_unique = []
                models_dict = {}
                for i in range(0, len(json_data_evaluate)):
                    if json_data_evaluate[i][3] not in models_unique:
                        models_unique.append(json_data_evaluate[i][3])
                        models_dict[json_data_evaluate[i][3]] = json_data_evaluate[i][1]['mean_accuracy']

                avg_accuracy = 0
                for key, value in models_dict.items():
                    avg_accuracy = avg_accuracy + value
                if len(models_dict) > 0:
                    avg_accuracy = round(avg_accuracy / len(models_dict), 2)
                else:
                    avg_accuracy = 0

                if len(models_unique) > 3:
                    avg_accuracy_last = 0
                    for i in range(1, 4):
                        avg_accuracy_last += models_dict[models_unique[len(models_unique) - i]]
                    avg_accuracy_last = round(avg_accuracy_last / 3, 2)
                else:
                    avg_accuracy_last = avg_accuracy

                if avg_accuracy == 0 and avg_accuracy_last == 0:
                    delta_accuracy = 0
                elif avg_accuracy == 0:
                    delta_accuracy = -100
                elif avg_accuracy_last == 0:
                    delta_accuracy = 100
                elif avg_accuracy_last > avg_accuracy:
                    delta_accuracy = round(100 - ((avg_accuracy * 100) / avg_accuracy_last), 2)
                else:
                    delta_accuracy = round(100 - ((avg_accuracy_last * 100) / avg_accuracy), 2) * -1

                st.metric(label=model.accuracyTitle, value=avg_accuracy, delta=str(delta_accuracy) + "%",
                          delta_color="inverse")

            st.markdown("---")


        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.write(model.titleInferencePerformance)

                models_dict = {}

                models = []
                for i in range(0, len(json_data_inference)):
                    models.append(json_data_inference[i][3])

                models_unique = []
                for item in models:
                    if item not in models_unique:
                        models_unique.append(item)

                for i, key in enumerate(models_unique):
                    models_dict[key] = []

                for i in range(0, len(json_data_inference)):
                    models_dict[json_data_inference[i][3]].append(round(json_data_inference[i][0]))

                data = pd.DataFrame(models_dict)
                st.line_chart(data)

            with col2:
                st.write(model.titleModelEval)

                models_unique = []
                models_dict = {}
                for i in range(0, len(json_data_evaluate)):
                    if json_data_evaluate[i][3] not in models_unique:
                        models_unique.append(json_data_evaluate[i][3])
                        models_dict[json_data_evaluate[i][3]] = [json_data_evaluate[i][1]['accuracies']]

                data = pd.DataFrame(models_dict, index=[0])
                st.line_chart(data)

        st.markdown("---")

        with st.container():
            col1, col2, col3 = st.columns(3)

            with col1:
                with st.container():
                    st.write(model.titleDataAnnotation)

                    total, completed, in_progress = self.calculate_annotation_stats(model)

                    data = pd.DataFrame({"Status": ["Completed", "In Progress"], "Value": [completed, in_progress]})

                    # Create a horizontal bar chart
                    chart = alt.Chart(data).mark_bar().encode(
                        x='Value',
                        y=alt.Y('Status', sort='-x'),
                        color=alt.Color('Status')
                    )

                    st.altair_chart(chart)
            with col2:
                with st.container():
                    st.write(model.titleDatasetInfo)

                    # Use mock data when API is not available
                    response = type('MockResponse', (), {
                        'status_code': 200, 
                        'json': lambda self: {
                            "splits": [
                                {"name": "dataset_1", "size": 1500, "type": "training", "number_of_rows": 1500},
                                {"name": "dataset_2", "size": 800, "type": "validation", "number_of_rows": 800},
                                {"name": "dataset_3", "size": 300, "type": "test", "number_of_rows": 300}
                            ]
                        }
                    })()

                    # Check if the request was successful (status code 200)
                    names = []
                    rows = []
                    if response.status_code == 200:
                        # Convert the response content to a JSON object
                        json_data = response.json()

                        for i in range(0, len(json_data['splits'])):
                            names.append(json_data['splits'][i]['name'])
                            rows.append(json_data['splits'][i]['number_of_rows'])
                    else:
                        print(f"Error: Unable to fetch data from the API (status code {response.status_code})")

                    data = pd.DataFrame({"Dataset": names, "Value": rows})

                    # Create a horizontal bar chart
                    chart = alt.Chart(data).mark_bar().encode(
                        x='Value',
                        y=alt.Y('Dataset', sort='-x'),
                        color=alt.Color('Dataset')
                    )

                    st.altair_chart(chart)
            with col3:
                with st.container():
                    st.write(model.titleTrainingPerformance)

                    models_dict = {}

                    for i in range(0, len(json_data_training)):
                        models_dict[i] = round(json_data_training[i][0])

                    data = pd.DataFrame({"Runs": models_dict.keys(), "Value": list(models_dict.values())})

                    # Create a horizontal bar chart
                    chart = alt.Chart(data).mark_bar().encode(
                        x='Value',
                        y=alt.Y('Runs', sort='-x'),
                        color=alt.Color('Runs')
                    )

                    st.altair_chart(chart)

        st.markdown("---")

        with st.container():
            st.write(model.titleEvaluationPerformance)

            runs_dict = {}

            for i in range(0, len(json_data_evaluate)):
                runs_dict[i] = round(json_data_evaluate[i][0])

            data = pd.DataFrame({"Runs": runs_dict.keys(), "Value": list(runs_dict.values())})

            # Create a horizontal bar chart
            chart = alt.Chart(data).mark_bar().encode(
                x='Value',
                y=alt.Y('Runs', sort='-x'),
                color=alt.Color('Runs')
            )

            st.altair_chart(chart)


    def calculate_annotation_stats(self, model):
        completed = 0
        in_progress = 0
        data_dir_path = Path(model.annotation_files_dir)

        for file_name in data_dir_path.glob("*.json"):
            with open(file_name, "r") as f:
                data = json.load(f)
                v = data['meta']['version']
                if v == 'v0.1':
                    in_progress += 1
                else:
                    completed += 1
        total = completed + in_progress

        status_json = {
            "annotations": [
                {
                    "completed": completed,
                    "in_progress": in_progress,
                    "total": total
                }
            ]
        }

        with open(model.status_file, "w") as f:
            json.dump(status_json, f, indent=2)

        return total, completed, in_progress
