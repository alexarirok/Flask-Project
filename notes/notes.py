  {{ form.hidden_tag() }}
      <fieldset>
        <legend>Sign Up</legend>
        <div>
          {{ form.email.label(class="form-control-label") }}

            {% if form.email.errors %}
              {{ form.email(class="form-control form-control-lg is-invalid") }}

              <div class="is-invalid-feedback">

                {% for error in form.email.errors %}
                <span> {{ error }}</span>
                {% endfor %}

              </div>
              {% else %}
                {{ form.email(class="form-control form-control-lg") }}

              {% endif %}

        </div>
        


      </fieldset>
    </form>
 </div>

{% endblock %}