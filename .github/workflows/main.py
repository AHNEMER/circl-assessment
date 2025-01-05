name: Deploy main branch

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  DeployServerless:
    name: Deploy
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [14]
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2
        with:
          persist-credentials: false

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v1
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install Dependencies
        run: npm install

      - name: Serverless Deploy
        uses: serverless/github-action@master
        with:
          args: deploy
        env:
          LOG_LEVEL: debug
          AWS_ACCESS_KEY_ID: AKIAQ4J5YL6LZQUX4ZME
          AWS_SECRET_ACCESS_KEY: 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
