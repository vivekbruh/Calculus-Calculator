
import * as THREE from 'three'
import { NeverStencilFunc } from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
//import { GLTFLoader } from 'https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/GLTFLoader.js';
//import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
//import { GLTFLoader } from "./GLTFLoader.js";


const scene = new THREE.Scene();
console.log('test');
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({
    canvas: document.querySelector('#bg'), alpha:true
});
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight)
camera.position.setZ(-40);
camera.position.setX(-3);
camera.position.setY(-3);

scene.background = new THREE.Color(0xffffff);





//console.log("test2132131");

/*
let obj;
const loader = new GLTFLoader()
loader.load('scene.gltf', function (gltf) {
        obj = gltf.scene;
        scene.add(gltf.scene)
    },
    (xhr) => {
        console.log((xhr.loaded / xhr.total) * 100 + '% loaded')
    },
    (error) => {
        console.log(error)
    }
)
*/





var light1 = new THREE.AmbientLight(0xffffff);
scene.add(light1);
scene.background = new THREE.Color(0x030613)


//const geometry = new THREE.TorusGeometry(10, 3, 16, 100);
const material = new THREE.MeshBasicMaterial({color: 0x5889a7, wireframe: true});
const material1 = new THREE.MeshBasicMaterial({color: 0xaa7cc5, wireframe: true});
//const torus = new THREE.Mesh(geometry, material);
//scene.add(torus);

const geometry1 = new THREE.ConeGeometry( 1.62, 2.1, 8 );






let particle = new THREE.Object3D();
scene.add(particle);

for (var i = 0; i < 400; i++) 
{
    if (i%3==0)
    {
        var mesh = new THREE.Mesh(geometry1, material1);
    }
    else
    {
        var mesh = new THREE.Mesh(geometry1, material);
    }
    mesh.position.set(Math.random() - 0.5, Math.random() - 0.5, Math.random() - 0.5).normalize();
    mesh.position.multiplyScalar(90 + (Math.random() * 350));
    mesh.rotation.set(Math.random() * 2, Math.random() * 2, Math.random() * 2);
    
    particle.add(mesh);
}




const controls = new OrbitControls(camera, renderer.domElement);
controls.enablePan = false;
controls.minDistance = 15;
controls.maxDistance = 50;



let t = true;
function animate(){
    console.log(t);
    requestAnimationFrame(animate);


    particle.rotation.x += 0.002;
    //particle.rotation.y -= 0.0040;
    
    if (camera.position.z <= 50 && t == true)
    {
        if (camera.position.z > 49)
        {
            t = false;
            console.log(t)
        }
        camera.position.z += 0.1;
        //console.log("camera position" + camera.position.z)
    }
    if (camera.position.z >= -50 && t == false)
    {
        if (camera.position.z < -49)
        {
            t = true;
        }
        camera.position.z -= 0.1;
        //console.log("camera position" + camera.position.z)
    }
    
    controls.update();
    renderer.render(scene, camera);
}


animate();






