import { useEffect, useState } from "react";

function useIncrement(initValue = 0, step = 1) {
	const [count, setCount] = useState(initValue);

	function incrementer() {
		setCount((c) => {
			console.log("c = ", c);
			return c + step;
		});
	}

	return [count, incrementer];
}

function useAutoIncrement(initValue = 0, step = 1) {
	const [count, setCount] = useState(initValue);

	useEffect(() => {
		const timer = window.setInterval(() => {
			setCount((c) => (c < 10 ? (c + step) : 0));
		}, 1000);

		return () => clearInterval(timer);
	}, []);

	function incrementer() {
		setCount((c) => {
			console.log("c = ", c);
			return c + step;
		});
	}

	return [count, incrementer];
}

function Compteur() {
	const [count, incrementer] = useAutoIncrement();

	return <button onClick={incrementer}>Incrémenter {count}</button>;
}

export default Compteur;
