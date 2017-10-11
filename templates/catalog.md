Пицца из нашего меню:

{% for title, choices in catalog|groupby('title') %}
*{{ title }}*
{% for pizza in choices %}{%- if loop.first %}{{ pizza.description }}{% endif %}
*{{ pizza.pizza_id }}* / {{ pizza.height_cm }}см ({{ pizza.weight_gr }}гр) - *{{ pizza.price }} руб.*
{%- endfor %}
{% endfor %}
