import '../styles/Banner.css'
import logo from '../assets/logo.png'

function Banner(){
    return <div className="Title">
         <img src={logo} alt='La maison jungle' id='logo' className='lmj-logo' />
         <h1>~La maison jungle</h1>
         </div>
}
export default Banner