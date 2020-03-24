all: 04-graphics-outputs/double-up-raw-attributes.png

03-processed-data/mansfield-double-up-course-data.csv: 02-raw-data/mansfield-double-up-course.gpx 01-code-scripts/extract_gpx_data.py
	python 01-code-scripts/extract_gpx_data.py

03-processed-data/mansfield-double-up-course-data-enhanced.csv: 03-processed-data/mansfield-double-up-course-data.csv 01-code-scripts/process_gpx_data.py
	python 01-code-scripts/process_gpx_data.py

04-graphics-outputs/double-up-raw-attributes.png: 03-processed-data/mansfield-double-up-course-data-enhanced.csv 01-code-scripts/visualize_gpx_data.py
	python 01-code-scripts/visualize_gpx_data.py

# paper/report.pdf: paper/report.md figures/awesome_plot.png
# 	pandoc paper/report.md -o paper/report.pdf

clean:
#	rm -f paper/report.pdf
#	rm -f figures/*.png
	rm -f 04-graphics-outputs/*.png
	rm -f 03-processed-data/*.csv
