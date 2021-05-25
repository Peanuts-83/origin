import '../styles/ShoppingList.css'
import { plantList } from '../datas/plantList'

function ShoppingList() {
    const categories = plantList.reduce(
        (acc, plant) => 
            acc.includes(plant.category) ? acc : acc.concat(plant.category), []
    )

	return (
    <div>
        <ol class='lmj-plant-list'>
            {categories.map((cat) => (
                <li key={cat}>{cat}</li>
            ))}
        </ol>
        <ul class='lmj-plant-item'>
            {plantList.map((plant) => (
                <li key={plant.id}>
                    {plant.isSpecialOffer ? <span class='lmj-sales'>{plant.name + ' -> promo!'}</span> : plant.name + ' '} 
                    {plant.isBestSale && <span>🔥</span>}
                    {}
                </li>
            ))}
	    </ul>
    </div>)
}

export default ShoppingList