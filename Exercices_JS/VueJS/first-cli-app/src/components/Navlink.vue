<script>
export default {
	name: 'Navlink',
  props: ['url','text']
}
</script>

<template>
	<a :href="url"><b>{{ text }}</b></a>
</template>

<style>
	a {
		text-decoration: none;
	}
</style>