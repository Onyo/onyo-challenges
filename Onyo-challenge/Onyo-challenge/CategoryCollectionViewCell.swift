//
//  CategoryCollectionViewCell.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/15/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit
import AlamofireImage

class CategoryCollectionViewCell: UICollectionViewCell {

    // MARK: - Properties
    
    @IBOutlet var categoryImage: UIImageView!
    @IBOutlet var categoryName: UILabel!
    
    // MARK: - Life Cycle
    
    override func prepareForReuse() {
        categoryImage.image = nil
    }
    
    // MARK: - Configure Cell
    
    func configureCellWith(category: Category) {
        if let imageURL = category.imageMainURL {
            categoryImage.af_setImageWithURL(NSURL(string: imageURL)!, placeholderImage: nil, filter: AspectScaledToFillSizeFilter(size: categoryImage.bounds.size))
        }
        
        categoryName.text = (category.displayName?.uppercaseString)!
    }
}
