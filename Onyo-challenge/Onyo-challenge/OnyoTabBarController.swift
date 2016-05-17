//
//  OnyoTabBarController.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/15/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit

enum TabIndexes: Int {
    case HomeIndex = 0,
         CategoriesIndex = 1,
         CartIndex = 2
}

class OnyoTabBarController: UITabBarController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        selectedIndex = TabIndexes.CategoriesIndex.rawValue
    }
    
}
