#!/usr/bin/python
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

posts = {}
with open("posts") as f:
    posts_api_results = json.loads(f.read())

posts = posts_api_results['results']

content_lengths = {}
for post in posts:
    post_type = post['json_metadata']['type']
    body_length = len(post['body'])
    if not post_type in content_lengths:
        content_lengths[post_type] = []
    content_lengths[post_type].append(body_length)

for post_type in content_lengths:
    mean = np.mean(content_lengths[post_type])
    median = np.median(content_lengths[post_type])
    plt.figure(figsize=(12, 6))
    plt.hist(content_lengths[post_type], bins=20)
    plt.axvline(mean, color='red', linestyle='solid', \
                linewidth=2, label="Mean content length: %d chars" % mean)
    plt.gca().add_patch(patches.Rectangle((mean-500, 0), \
                                          1000, max(content_lengths[post_type]), \
                                          color="green", alpha=0.5, \
                                          label="Body length in average"))
    plt.axvline(median, color='orange', linestyle='solid', \
                linewidth=2, label="Median content length: %d chars" % median)
    plt.title("Content lengths for category \"%s\"" % post_type)
    plt.xlabel("Content length (chars)")
    plt.ylabel("Occurences")
    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.savefig("%s.png" % post_type)
