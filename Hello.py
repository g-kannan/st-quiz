# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Welcome to the quiz",
        page_icon="👋",
    )

    # Define the quiz data
    quiz_data = [
        {
            'question': 'Convert RDD to dataframe',
            'options': ['df = rdd.toDF()', 'df = rdd.todataframe()'],
            'correct_answer': 'df = rdd.toDF()',
        },
        {
            'question': 'Read delta table and save as dataframe',
            'options': ['df = spark.query("select * from tbl")','df = spark.read.table(table_name)'],
            'correct_answer': 'df = spark.read.table(table_name)',
        },
    ]

    # Create a Streamlit app
    st.title('Quiz App')

    score = 0

    for i, question in enumerate(quiz_data):
        st.subheader(f'Question {i + 1}: {question["question"]}')
        selected_option = st.radio('Options', question['options'])

        if selected_option == question['correct_answer']:
            score += 1

    st.write(f'Your score: {score}/{len(quiz_data)}')


if __name__ == "__main__":
    run()
